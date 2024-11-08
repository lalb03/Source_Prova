import os, sys

def delete_file(tex_file):
    pdf_file = tex_file.replace("DocsSource/", "Documents/").replace(".tex", ".pdf")
    try:
        if os.path.exists(pdf_file):
            os.remove(pdf_file)
            print(f"Deleted PDF file: {pdf_file}")
        else:
            print(f"{pdf_file} does not exist, skipping.")

        dir = os.path.dirname(tex_file)
        if not os.listdir(dir):
            os.rmdir(dir)
            print(f"Directory eliminata: {dir}")
    except FileNotFoundError:
        print(f"{pdf_file} does not exist.")
    except Exception as e:
        print(f"Error deleting {pdf_file}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python delete_file.py <path_to_tex_file")
    else:
        delete_file(sys.argv[1])
