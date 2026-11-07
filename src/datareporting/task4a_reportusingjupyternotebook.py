import nbformat as nbf
import nbconvert as nbc
import markdown
from pathlib import Path
import matplotlib.pyplot
import matplotlib.pyplot as plt


def convert_markdown_topng(markdown_text, output_filename="executive_performance_dashboard.png", output_dir="./data/output/"):
    # 1. Ensure the output directory exists
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract just the filename in case a full path was passed into the filename parameter
    final_filename = Path(output_filename).name
    
    # 2. Convert Markdown to HTML and inject clean, readable styles for Visual Studio Viewer
    html_body = markdown.markdown(markdown_text)
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 40px;
                color: #222222;
                background-color: #ffffff;
                line-height: 1.6;
                width: 800px; /* Fixed width prevents the image from breaking layout constraints */
            }}
            h1 {{ color: #1a365d; border-bottom: 2px solid #cbd5e0; padding-bottom: 8px; margin-bottom: 20px; }}
            h2 {{ color: #2c5282; margin-top: 25px; }}
            pre {{ background-color: #f7fafc; padding: 15px; border: 1px solid #e2e8f0; border-radius: 6px; font-family: Consolas, monospace; overflow-x: auto; }}
            code {{ font-family: Consolas, monospace; background-color: #edf2f7; padding: 2px 6px; border-radius: 4px; color: #c53030; }}
            pre code {{ background-color: transparent; padding: 0; color: #2d3748; }}
            p {{ margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    
    # 3. Use your local browser engine to snap a high-quality PNG screenshot

def generate_jupyter_template(input_path):
    nb = nbf.v4.new_notebook()

    # Define cells to be added dynamically
    cells = [
        nbf.v4.new_markdown_cell(
            "# Executive Performance Report\n*Generated Dynamically*"
        ),
        nbf.v4.new_code_cell(
            "import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n"
            "sns.set_theme(style='whitegrid')\nprint('Environment configured successfully.')"
        ),
        # Dynamically injected structural path using safely handled repr string
        nbf.v4.new_code_cell(
            f"# Load the dynamic dataset path\ninput_path = {repr(input_path)}\ndf = pd.read_csv(input_path)\ndf.head()"
        ),
    ]

    nb["cells"] = cells

    # Write out the structural file
    output_filename = "./data/output/executive_performance.ipynb"
    
    # Ensure directory framework exists before writing
    Path("./data/output").mkdir(parents=True, exist_ok=True)
    
    with open(output_filename, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    notebook_path = output_filename

    # Load the notebook file
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbf.read(f, as_version=4)

    # Convert the notebook structure into a readable markdown/plain text format
    markdown_exporter = nbc.MarkdownExporter()
    body, _ = markdown_exporter.from_notebook_node(notebook_content)
    
    # Convert body text into image
    convert_markdown_topng(body, output_filename="report_output.png", output_dir="./data/output/")
    
    # Print the formatted template directly to the output window
    print(body)
    print(f"Success: Dynamic Jupyter template saved as '{output_filename}'")

# Example invocation string path 
if __name__ == "__main__":
    generate_jupyter_template('./data/input/AusApparalSales4thQrt2020.csv')
