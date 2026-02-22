using System.Security.Cryptography;
using MyApp;

namespace MyApp
{
    class Program
    {
        public static byte[] a = {0x35,0xe8,0x5b,0x93,0x90,0xd3,0x1c,0xdf,0xfd,0x4d,0x0b,0x1c,0x50,0x77,0x3c,0x2a,0xb8,0xca,0x5f,0xe4,0xc9,0x17,0x4a,0x57,0x01,0x6b,0x27,0xa3,0x01,0xc8,0x87,0xc5,0x08,0xee,0x78,0x3c,0xd4,0xb2,0x39,0xc7,0x79,0x07,0x11,0xba,0xd7,0xc0,0xd0,0x69,0xc2,0x45,0x10,0xae,0x16,0x06,0xc0,0xe5,0x9f,0x95,0xd0,0xb9,0xf0,0x69,0xec,0x4d};
        public static byte[] b = {0x68,0x6f,0x70,0x65,0x5f,0x79,0x6f,0x75,0x5f,0x65,0x6e,0x6a,0x6f,0x79,0x21,0x21};
        public static byte[] c = {0x31,0x76,0x33,0x5f,0x6e,0x33,0x76,0x33,0x72,0x5f,0x67,0x30,0x74,0x5f,0x31,0x76};


        static void Main(string[] args)
        {
            Console.WriteLine("Enter the flag:");
            string? userInput = Console.ReadLine();
            if (userInput == null) {
                Console.WriteLine("Invalid input!");
                return;
            }

            var B = global::B.B.b();

            if (!E.E.e(
                D.D.d(
                    C.C.c(
                        B,
                        A.A.a(Z.Z.z())
                    )
                ),
                B,
                userInput
            ).SequenceEqual(a))
            {
                Console.WriteLine("Wrong flag!");
            } else {
                Console.WriteLine("Correct flag!");
            }
        }
    }
}

namespace A {
    class A {
        public static ICryptoTransform a(Aes a) {
            return a.CreateEncryptor(Program.b, Program.c); 
        }
    }
}
namespace B {
    class B {
        public static MemoryStream b() {
            return new MemoryStream();
        }
    }
}
namespace C {
    class C {
        public static CryptoStream c(MemoryStream a, ICryptoTransform b) {
            return new CryptoStream(a, b, CryptoStreamMode.Write); 
        }
    }
}
namespace D {
    class D {
        public static StreamWriter d(CryptoStream d) {
            return new StreamWriter(d);
        }
    }
}
namespace E {
    class E {
        public static byte[] e(StreamWriter a, MemoryStream b, string c) {
            a.Write(c); 
            a.Flush();
            a.Close();

            return b.ToArray();
        }
    }
}

namespace Z {
    class Z {
        public static Aes z() {
            return Aes.Create();
        }
    }
}