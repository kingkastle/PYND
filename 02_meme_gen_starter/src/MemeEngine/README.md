# Meme Engine

### Class name: 
```MemeEngine```

### General description
This class is responsible of building a meme (a meme is a picture that includes a quote and the corresponding author) and save it locally in a destination folder.
In order to build a meme, the attributes for this class are:
 * ```img_path```: path to input image
 * ```text```: quote
 * ```author```: quote's author
 * ```width```: image width
 
The only method for this class is ```make_meme()``` which is responsible of building and save the meme in a local folder.

### module's dependencies
Module consumes the Pillow library: 
```
Pillow==7.0.0
```
Also, the standard library module: ``os``

### examples
```
quote = "Hola, que tal?"
author = "Rafa"
img_path = "/homeuser/rafa/dog.png"

destination_folder ="/homeuser/rafa/Downloads/" 

meme = MemeEngine(destination_folder)

path = meme.make_meme(img_path, quote, author)

print(f"Meme generated @: {path}")

```


