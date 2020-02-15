from PIL import Image, ImageDraw # , ImageFont
import os

class MemeEngine:

    def __init__(self, dst_folder):
        self.dst_folder = dst_folder

    def make_meme(self, img_path, text, author, width=500):
        """Create a Postcard With a Text Greeting

        Arguments:
            img_path {str} -- the desired location for the output image.
            text (str) --- quote body
            author (str) -- quote author
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        # this encoding is required to avoid issues with files
        text = text.encode("utf-8")
        text = str(text, "latin-1")
        draw.text((10, 30), f'{text} {author}', fill='white') # , font=font

        out_path = self.dst_folder +  "/" + os.path.basename(img_path)
        img.save(out_path)
        return out_path
