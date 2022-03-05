
echo "Running hugo-obsidian"

hugo-obsidian -input=content/garden -output=static -index -root=.

echo "--------------"
echo "Running python script to clean up paths"

python clean_index_paths.py
echo "--------------"
echo "Done."
