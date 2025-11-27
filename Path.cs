using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pretty_girl_face_maker
{
    public class Path
    {
        private readonly string _path;

        public Path(string path)
        {
            _path = path;
        }

        public static implicit operator string(Path p) => p._path;
        public static implicit operator Path(string s) => new Path(s);

        public static Path operator /(Path left, Path right)
        {
            return new Path(System.IO.Path.Combine(left._path, right._path));
        }

        public override string ToString()
        {
            return _path;
        }
        public Path ParentPath
        {
            get
            {
                string parent = System.IO.Path.GetDirectoryName(_path);
                return parent != null ? new Path(parent) : null;
            }
        }

        public Path RelativeTo(Path basePath)
        {
            Uri baseUri = new Uri(basePath._path.EndsWith("\\")
                                  ? basePath._path
                                  : basePath._path + "\\");
            Uri targetUri = new Uri(_path);
            Uri relativeUri = baseUri.MakeRelativeUri(targetUri);
            string relativePath = Uri.UnescapeDataString(relativeUri.ToString());
            return new Path(relativePath.Replace("/", "\\\\"));
        }

        public string FileName => System.IO.Path.GetFileName(_path);
    }
}
