using System.Windows.Forms;

namespace pretty_girl_face_maker
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            natsPreview = new PictureBox();
            imageDisTabs = new TabControl();
            resetBtn = new Button();
            saveBtn = new Button();
            clipboardBtn = new Button();
            ((System.ComponentModel.ISupportInitialize)natsPreview).BeginInit();
            SuspendLayout();
            // 
            // natsPreview
            // 
            natsPreview.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Right;
            natsPreview.Location = new Point(367, 12);
            natsPreview.Name = "natsPreview";
            natsPreview.Size = new Size(421, 397);
            natsPreview.SizeMode = PictureBoxSizeMode.Zoom;
            natsPreview.TabIndex = 1;
            natsPreview.TabStop = false;
            // 
            // imageDisTabs
            // 
            imageDisTabs.Dock = DockStyle.Left;
            imageDisTabs.Font = new Font("Comic Sans MS", 9F, FontStyle.Regular, GraphicsUnit.Point, 0);
            imageDisTabs.Location = new Point(0, 0);
            imageDisTabs.Name = "imageDisTabs";
            imageDisTabs.SelectedIndex = 0;
            imageDisTabs.Size = new Size(361, 450);
            imageDisTabs.TabIndex = 2;
            // 
            // resetBtn
            // 
            resetBtn.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            resetBtn.Location = new Point(367, 415);
            resetBtn.Name = "resetBtn";
            resetBtn.Size = new Size(143, 23);
            resetBtn.TabIndex = 3;
            resetBtn.Text = "reset nats";
            resetBtn.UseVisualStyleBackColor = true;
            resetBtn.Click += resetBtn_Click;
            // 
            // saveBtn
            // 
            saveBtn.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            saveBtn.Location = new Point(650, 415);
            saveBtn.Name = "saveBtn";
            saveBtn.Size = new Size(138, 23);
            saveBtn.TabIndex = 4;
            saveBtn.Text = "save to disk";
            saveBtn.UseVisualStyleBackColor = true;
            // 
            // clipboardBtn
            // 
            clipboardBtn.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            clipboardBtn.Location = new Point(516, 415);
            clipboardBtn.Name = "clipboardBtn";
            clipboardBtn.Size = new Size(128, 23);
            clipboardBtn.TabIndex = 5;
            clipboardBtn.Text = "python clipboard";
            clipboardBtn.UseVisualStyleBackColor = true;
            clipboardBtn.Click += clipboardBtn_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(clipboardBtn);
            Controls.Add(saveBtn);
            Controls.Add(resetBtn);
            Controls.Add(imageDisTabs);
            Controls.Add(natsPreview);
            Name = "Form1";
            Text = "FOIDGENERATOR9000";
            FormClosed += Form1_FormClosed;
            ((System.ComponentModel.ISupportInitialize)natsPreview).EndInit();
            ResumeLayout(false);
        }

        #endregion
        private PictureBox natsPreview;
        private TabControl imageDisTabs;
        private Button resetBtn;
        private Button saveBtn;
        private Button clipboardBtn;
    }
}
