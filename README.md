🗂️ JSON ➜ CSV Converter (Python)






A lightweight and beginner-friendly Python tool to convert JSON files into CSV format with just one command.
Perfect for data cleaning, Excel imports, analytics, and automation.

✨ Features

🔄 Converts any valid .json file to .csv

🧠 Auto-detects JSON structure (list or dict)

⚠️ Error handling for invalid/missing files

🪶 Zero dependencies (optional pandas support)

🖥️ CLI-friendly — run with a single command

📁 Project Structure
json-to-csv/
│── convert.py
│── input.json
│── output.csv        (generated)
│── README.md

📦 Installation
1. Clone the repository
git clone https://github.com/<your-username>/json-to-csv.git
cd json-to-csv

2. (Optional) Install pandas

If your script uses pandas:

pip install pandas

▶️ Usage
Run the converter
python convert.py input.json output.csv


If your script doesn’t require arguments and uses default names:

python convert.py

Input JSON Example
[
  { "name": "John", "age": 30 },
  { "name": "Anna", "age": 25 }
]

Output CSV
name,age
John,30
Anna,25

⚙️ Requirements

Python 3.8 or newer

Works on Windows, Mac, Linux

📝 Notes

If using Git on Windows, avoid working directly inside C:/ to prevent “dubious ownership” errors.

Ideal folder for coding:

C:\Users\Administrator\Documents\projects\

🤝 Contributing

Pull requests and suggestions are welcome!
Feel free to open an issue if you’d like new features such as:

🧩 Nested JSON flattening

📊 CSV delimiter customization

🧪 GUI version

📜 License

This project is licensed under the MIT License.