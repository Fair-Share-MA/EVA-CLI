# FSA-EVA-CLI

## Usage:

1. Install python version 3.9.x
2. Run `pip install -r requirements.txt` in the root folder
3. Create folders named `input` and `output` at the same level as the `src` directory
4. Add any comparision overrides by creating a new key value pair in `mime_types.json -> comparision_overrides`. See example below for more information
5. Move all excel or csv files to be processed into the `input` directory. You may also use a previously generated `export.csv` file as an input to build on the previous dataset
6. Run the script with `python main.py` from within the src folder.
7. Wait for export to complete. You should see `export.csv` in the output folder.

---

## Comparision overrides:

A comparision override is a ket value pair that overrides the string matching algorithm normally used. For example:

```
{
    "voter id": ["voter_id", "voter_registration_id"]
}
```

The key is the trigger. When merging 2 files, if the algorithm comes across `voter id` in the first file, it will try and match it to either `voter id`, `voter_id`, or `voter_registration_id` in the second file. If none of these are found in the second file, the normal string matching algorithm will be used.
