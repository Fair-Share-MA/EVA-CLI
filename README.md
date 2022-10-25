# FSA-EVA-CLI

## Usage:

1. Install python version 3.9.x
2. Run `pip install -r requirements.txt` in the root folder
3. Create folders named `input` and `output` at the same level as the `src` directory
4. Move all excel or csv files to be processed into the `input` directory. You may also use a previously generated `export.csv` file as an input to build on the previous dataset
5. Run the script with `python main.py` from within the src folder.
6. Wait for export to complete. You should see `export.csv` in the output folder.
