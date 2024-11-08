import os, sys, subprocess

def compile_tex(tex_file):
    output_dir = os.path.join("Documents", os.path.dirname(tex_file))
    print(f"output: {output_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    command = [
        'latexmk', '-pdf', '-output-directory=' + output_dir, tex_file
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Error compiling file {tex_file}")


    clean_command = [
        'latexmk', '-c', '-output-directory=' + output_dir, tex_file
    ]
    try:
        subprocess.run(clean_command, check=True)
    except subprocess.CalledProcessError:
        print(f"Error clean file {tex_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compile_tex_file.py <path_to_tex_file>")
    else:
        compile_tex(sys.argv[1])