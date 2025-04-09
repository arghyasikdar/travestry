# travestry
A directory traversal tool writen in Python.

1. Clone the Repository

```
git clone https://github.com/arghyasikdar/traversty.git

```

2. Navigate to the Project Directory

```
cd traversty

```

4. Make the Script Executable (Optional)

```

chmod +x traversty.py

```

6. (Optional) Create a Symlink to run from anywhere


```

sudo ln -s $(pwd)/traversty.py /usr/local/bin/traversty

```

Now you can simply run traversty from any directory!

⚙️ Usage
You can run Traversty using:

```

python3 traversty.py -u <target_url> -w <wordlist_file>


```

or if you created the symlink:

```

traversty -u <target_url> -w <wordlist_file>

```

```
Command-Line Options:
Option	Description
-u, --url	Target URL (e.g., http://example.com)
-w, --wordlist	Path to the wordlist file
-v, --version	Display version information and exit
-h, --help	Show help message and usage options

```

📌 Example

```

python3 traversty.py -u http://testphp.vulnweb.com -w common_traversals.txt

```

OR if symlinked:

```

traversty -u http://testphp.vulnweb.com -w common_traversals.txt

```

⚡ Features

Fast directory traversal fuzzing 🚀

Beautiful colored output 🎨

Handles timeouts and connection errors gracefully 🤝

Lightweight and easy to use ⚡

⚠️ Disclaimer
This tool is intended for educational and authorized penetration testing purposes only.
Unauthorized usage against targets without consent is illegal.
