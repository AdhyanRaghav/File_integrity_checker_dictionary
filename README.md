# File_integrity_checker_dictionary

🛡️ File Integrity Checker (CLI)

A Python-based File Integrity Monitoring (FIM) tool that detects file tampering by comparing SHA-256 hashes of files against a trusted baseline snapshot.

This project was built from scratch to deeply understand how integrity monitoring systems work internally.

📌 Why This Tool?

In cybersecurity, maintaining file integrity is critical.

If even one byte changes in a file, its cryptographic hash changes completely.

This tool:

🔐 Creates a trusted baseline snapshot of file hashes

🔍 Detects modified, deleted, and newly created files

🧠 Uses dictionary-based comparison for fast integrity checking

⚙️ Implements chunk-based hashing for scalability

🚀 Features

✔️ SHA-256 hashing (cryptographic secure fingerprinting)
✔️ Chunk-based file reading (memory efficient)
✔️ Recursive directory scanning using os.walk()
✔️ Detects:

Modified files

Deleted files

New files
✔️ Clean anomaly-only reporting
✔️ Separate init and check modes

🛠️ Technologies Used
Library	Purpose
hashlib	Generate SHA-256 hashes
os	Traverse directories
json (optional upgrade)	Store baseline in structured format
Core Python	File I/O, dictionaries, control flow
📂 Project Structure
file-integrity-checker/
│
├── checker.py                  # Main CLI script
├── baseline.txt            # Auto-generated baseline (ignored in git)
├── target_files/           # Monitored directory (example)
├── README.md               # Documentation
└── .gitignore


.gitignore should contain:

baseline.txt
__pycache__/

⚙️ How to Run
🔹 Step 1 — Initialize Baseline
python checker.py


Select:

init


This:

Scans target directory

Computes SHA-256 hashes

Stores them in baseline.txt

🔹 Step 2 — Check Integrity

Run again:

python checker.py


Select:

check


The program will:

Load baseline

Recalculate hashes

Compare old vs new

Report anomalies

🧪 Example Output

If a file was modified:

File is modified: /path/to/file1.txt


If deleted:

File is deleted: /path/to/file2.txt


If new file added:

New file created: /path/to/malware.txt


If no changes:

No changes detected.

🧠 How It Works (Conceptual Flow)
Baseline Mode

Traverse directory recursively

For each file:

Create SHA-256 hash object

Read file in 4096-byte chunks

Update hash incrementally

Store:

file_path : hash

Check Mode

Load baseline into dictionary:

old_data[path] = hash


Generate new_data dictionary

Compare:

Missing in new → Deleted

Hash mismatch → Modified

Missing in old → New file

Print only anomalies

🔐 Security Considerations

⚠️ Current limitation:

If an attacker modifies both:

Target file

baseline.txt

The system will not detect tampering.

Future Improvements:

Baseline integrity verification

HMAC-based protection

Metadata monitoring (size, permissions, timestamps)

Proper CLI argument parsing (argparse)

GUI version

📈 What I Learned

While building this from scratch, I gained hands-on understanding of:

Cryptographic hashing (SHA-256)

Incremental hashing using .update()

Directory traversal using os.walk()

Dictionary-based comparison logic

Control flow design using flags

Security thinking beyond just “making it work”

This project strengthened my understanding of how real File Integrity Monitoring systems operate internally.

👨‍💻 Author

Adhyan Raghav
Cybersecurity Enthusiast
GitHub: https://github.com/AdhyanRaghav
