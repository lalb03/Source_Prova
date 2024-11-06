import os, shutil, subprocess

source_repo = 'DocsSource'
destination_repo = 'Documents'

def get_modified_files():
     os.chdir(source_repo)

     result = subprocess.run(
          ['git', 'diff', '--name-only', '--diff-filter=AMR', 'HEAD'],
          stdout=subprocess.PIPE,
          text=True
     )
     modified_files=[line for line in result.stdout.splitlines()
                      if line.endswith('.tex') and 'templates' not in line and 'Documenti Esterni/Verbali' not in line
                    ]
     os.chdir('..')
     return modified_files

def compile_tex(sorce_path, output_dir):
    command = [
        'latexmk', '-pdf', '-output-directory=' + output_dir, sorce_path
    ]
    subprocess.run(command, check=True)

def process_repo():
    modified_files = get_modified_files()

    for file in modified_files:
            tex_path=os.path.join(source_repo, file)
            relative_dir = os.path.dirname(file)
            output_dir = os.path.join(destination_repo, relative_dir)

            os.makedirs(output_dir, exist_ok=True)

            try:
                compile_tex(tex_path, output_dir)
                print(f"Successfully compiled: {tex_path}")
            except subprocess.CalledProcessError:
                print(f"Errore nella compilazione di {tex_path}")

if __name__ == "__main__":
    print(f"Compiling {source_path} to {output_dir}")
    process_repo()
