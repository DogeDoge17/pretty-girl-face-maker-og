using Accessibility;
using System.Diagnostics;
using System.Drawing.Imaging;
using System.Drawing.Text;
using System.Net;
using System.Runtime.CompilerServices;
using System.Text;

namespace pretty_girl_face_maker
{
    public partial class Form1 : Form
    {
        public Dictionary<string, List<ImageItem>> allFaceStiuff = new();
        public List<ImageItem> selectedFeatures = new();

        public Form1()
        {
            InitializeComponent();

            allFaceStiuff.Add("eyes", new());
            allFaceStiuff.Add("mouth", new());
            allFaceStiuff.Add("beat", new());
            allFaceStiuff.Add("nose", new());
            allFaceStiuff.Add("brows", new());
            allFaceStiuff.Add("extra", new());

            LoadImages();
            RegenNats();
            LoadDefaults();
        }

        private void LoadImages()
        {
            string[] keys = allFaceStiuff.Keys.ToArray();

            for (int i = 0; i < allFaceStiuff.Count; i++)
            {
                string[] files = Directory.GetFiles(new Path(System.Reflection.Assembly.GetEntryAssembly().Location).ParentPath / "images" / keys[i], "*.png", SearchOption.AllDirectories);

                var list = allFaceStiuff.ElementAt(i).Value;

                TabPage newTabPage = new TabPage(keys[i]);

                FlowLayoutPanel flowPanel = new FlowLayoutPanel();
                flowPanel.Dock = DockStyle.Fill;
                flowPanel.AutoScroll = true;
                flowPanel.WrapContents = true;
                flowPanel.FlowDirection = FlowDirection.LeftToRight;

                for (int j = 0; j < files.Length; j++)
                {
                    list.Add(new(files[j]));
                    Debug.WriteLine(files[j]);
                    list[j].ImagePreview = GeneratePreview(new Bitmap(list[j].Uri));
                    list[j].Category = keys[i];

                    list[j].Image = list[j].ImagePreview;
                    list[j].SizeMode = PictureBoxSizeMode.Zoom;
                    list[j].BorderStyle = BorderStyle.Fixed3D;
                    list[j].Size = new Size(100, 100); 
                    list[j].Click += natsImageClick;
                    flowPanel.Controls.Add(list[j]);
                }

                newTabPage.Controls.Add(flowPanel);
                imageDisTabs.Controls.Add(newTabPage);
            }
        }

        private void LoadDefaults()
        {
            int[] dI = [2, 0, -1, 0, 0,-1];

            for (int i = 0; i < Math.Min(dI.Length, allFaceStiuff.Count); i++)
            {
                if (dI[i] != -1)
                    natsImageClick(allFaceStiuff.ElementAt(i).Value[dI[i]], null);
            }
        }

        private Bitmap GeneratePreview(Bitmap bitmap)
        {
            //Bitmap bitmap = new Bitmap(imagePath);
            int minW = int.MaxValue, minH = int.MaxValue;
            int maxW = int.MinValue, maxH = int.MinValue;
            {
                Rectangle rect = new Rectangle(0, 0, bitmap.Width, bitmap.Height);

                BitmapData bmpData = bitmap.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);

                IntPtr ptr = bmpData.Scan0;
                int bytes = Math.Abs(bmpData.Stride) * bitmap.Height;
                byte[] pixelValues = new byte[bytes];

                System.Runtime.InteropServices.Marshal.Copy(ptr, pixelValues, 0, bytes);
                //bitmap.UnlockBits(bmpData);

                int pixelSize = 4; 

                for (int y = 0; y < bitmap.Height; y++)
                {
                    for (int x = 0; x < bitmap.Width; x++)
                    {
                        int index = (y * bmpData.Stride) + (x * pixelSize);

                        byte blue = pixelValues[index];    
                        byte green = pixelValues[index + 1]; 
                        byte red = pixelValues[index + 2]; 
                        byte alpha = pixelValues[index + 3]; 

                        if (alpha != 0)
                        {
                            if (minW > x) minW = x;
                            if (minH > y) minH = y;
                            if (maxW < x) maxW = x;
                            if (maxH < y) maxH = y;

                        }

                        //Console.WriteLine($"Pixel at ({x}, {y}): R={red}, G={green}, B={blue}, A={alpha}");
                    }
                }
                bitmap.UnlockBits(bmpData);
            }

            Debug.WriteLine($"({minW}, {minH}) ({maxW}, {maxH})");

            Rectangle sourceRect = new Rectangle(minW, minH, maxW - minW, maxH - minH);
            Bitmap ret = null;
            using (Bitmap croppedBitmap = new Bitmap(sourceRect.Width, sourceRect.Height))
            {
                using (Graphics g = Graphics.FromImage(croppedBitmap))
                {
                    g.DrawImage(bitmap, new Rectangle(0, 0, sourceRect.Width, sourceRect.Height), sourceRect, GraphicsUnit.Pixel);

                }
                ret = new(croppedBitmap);
            }
            bitmap.Dispose();
            return ret;
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            foreach (var stuff in allFaceStiuff)
            {
                foreach (var thing in stuff.Value)
                {
                    thing.ImagePreview.Dispose();
                }
            }
        }

        private void natsImageClick(object sender, EventArgs e)
        {
            ImageItem item = (ImageItem)sender;

            if (selectedFeatures.IndexOf(item) == -1)
            {
                if(item.Category != "extra")
                    ToggleOfType(item);
                selectedFeatures.Add(item);
                item.BackColor = Color.Green;
            }
            else
            {
                item.BackColor = Color.Transparent;
                selectedFeatures.Remove(item);
            }

            RegenNats();
        }

        private void ToggleOfType(ImageItem item)
        {
            for (int i = 0; i < selectedFeatures.Count; i++)
            {
                if (selectedFeatures[i].Category == item.Category)
                {
                    selectedFeatures[i].BackColor = Color.Transparent;
                    selectedFeatures.Remove(selectedFeatures[i]);
                }
            }
        }

        private void RegenNats()
        {
            if (natsPreview.Image != null)
                natsPreview.Image.Dispose();

            natsPreview.Image = null;

            using (Bitmap bp = new Bitmap(new Path(System.Reflection.Assembly.GetEntryAssembly().Location).ParentPath / "images" / "face.png"))
            {
                using (Graphics g = Graphics.FromImage(bp))
                {
                    for (int i = 0; i < selectedFeatures.Count; i++)
                    {                        
                        g.DrawImage(Image.FromFile(selectedFeatures[i].Uri), selectedFeatures[i].Uri.ToString().Contains("crossed") ? new Point(-18, -22) : new Point(0, 0));
                    }
                    g.Save();
                }

                natsPreview.Image = GeneratePreview(bp);
            }
        }

        private void resetBtn_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < selectedFeatures.Count; i++)
            {
                selectedFeatures[i].BackColor = Color.Transparent;
            }

            selectedFeatures.Clear();

            LoadDefaults();
            RegenNats();
        }

        private void clipboardBtn_Click(object sender, EventArgs e)
        {
            StringBuilder outp = new("$changeNatsukiEMR(");

            for (int i = 0; i < selectedFeatures.Count; i++)
            {
                if (selectedFeatures[i].Category != "extra")
                    outp.Append($"{selectedFeatures[i].Category}=\"{selectedFeatures[i].Uri.FileName}\"" + ((i != selectedFeatures.Count -1 ) ? ", " : ""));
                else if (selectedFeatures[i].Uri.ToString().Contains("left"))
                    outp.Append($"left=\"{selectedFeatures[i].Uri.FileName}\"" + ((i != selectedFeatures.Count - 1) ? ", " : ""));
                else if (selectedFeatures[i].Uri.ToString().Contains("right"))
                    outp.Append($"right=\"{selectedFeatures[i].Uri.FileName}\"" + ((i != selectedFeatures.Count - 1) ? ", " : ""));
                else if (selectedFeatures[i].Uri.ToString().Contains("crossed"))
                    outp.Append($"crossed=\"{selectedFeatures[i].Uri.FileName}\"" + ((i != selectedFeatures.Count - 1) ? ", " : ""));

            }

            outp.Append($")");

            Clipboard.SetText(outp.ToString());
        }
    }
}
