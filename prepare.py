import os
import shutil

_DATA_URL = {
    "train": [f"data/train_images_{i}/" for i in range(5)],
    "val": ["data/val_images/"],
    "test": ["data/test_images/"],
}

def move_files(sub):
    cache = {}
    path_sub = os.path.join("data", sub)
    if not os.path.exists(path_sub):
        os.mkdir(path_sub)
    for folder in _DATA_URL[sub]:
        for path in os.listdir(folder):
                if path.endswith(".JPEG"):
                    # image filepath format: <IMAGE_FILENAME>_<SYNSET_ID>.JPEG
                    root, _ = os.path.splitext(path)
                    _, synset_id = os.path.basename(root).rsplit("_", 1)
                    if not (synset_id in cache):
                        if not os.path.exists(f"data/{sub}/{synset_id}"):
                            os.mkdir(f"data/{sub}/{synset_id}")
                        cache[synset_id] = True
                    shutil.move(f"{folder}/{path}", f"data/{sub}/{synset_id}/{path}")


if __name__ == '__main__':
    move_files('train')

