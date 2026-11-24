import os

ENTRY = "Tip: the bug you're hunting lives in the file you swore you'd never touch, written by a past you who swore they'd document it. Go touch it. Your weekend is waiting."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
