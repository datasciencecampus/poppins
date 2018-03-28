# Stitched images

The outputs of the programs have been stitched together using ImageMagick:

```sh
for file in `ls outstanding | grep -v scores`; do 
  convert outstanding/$file good/$file \
          improve/$file inadequate/$file \
	  +append stitched/$file;
done
```

Thus, the output images have 4 wordclouds, from left to right in decreasing score.
