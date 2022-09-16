import argparse
import shutil
import sys
import time
import urllib
import zipfile
from pathlib import Path, PurePosixPath

import gdown
import numpy as np
from tqdm import tqdm


def download_url(url, dst):
    """Downloads file from a url to a destination.

    Args:
        url (str): url to download file.
        dst (str): destination path.
    """

    print(f'* url="{url}"')
    print(f'* destination="{dst}"')

    def _reporthook(count, block_size, total_size):
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time + 1e-6
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size + 1e-6)
        sys.stdout.write(
            "\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent, progress_size / (1024 * 1024), speed, duration)
        )
        sys.stdout.flush()

    if dst.exists():
        return
    else:
        urllib.request.urlretrieve(url, dst, _reporthook)
        sys.stdout.write("\n")


def extract_zip(src, dst):
    with zipfile.ZipFile(src, "r") as zf:
        for member in tqdm(zf.infolist(), desc="Extracting "):
            try:
                zf.extract(member, dst)
            except zipfile.error as err:
                print(err)


def prepare_market(dataset_path):
    # Market 1501 dataset
    market_1501_path = dataset_path / "Market1501"
    market_1501_zipfile = dataset_path / "market_1501.zip"
    url = "https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view?resourcekey=0-8nyl7K9_x37HlQm34MmrYQ"
    print("Download Market 1501 dataset")
    gdown.download(url, output=str(market_1501_zipfile), quiet=False, use_cookies=False, fuzzy=True)
    print("Extract Market 1501 dataset")
    extract_zip(market_1501_zipfile, dataset_path)
    Path(dataset_path / "Market-1501-v15.09.15").rename(market_1501_path)


def prepare_pa100k(dataset_path):
    # PA-100K dataset
    pa100k_path = dataset_path / "PA100k"
    pa100k_path.mkdir(parents=True, exist_ok=True)
    print("Download PA100k dataset")
    url = "https://drive.google.com/drive/folders/1d_D0Yh7C262gr0ef9EqkvG_M3fqgAWa2?usp=sharing"
    gdown.download_folder(url, output=str(pa100k_path), quiet=False, use_cookies=False)
    print("Extract PA100k dataset")
    extract_zip(pa100k_path / "data.zip", pa100k_path)


def prepare_peta(dataset_path):
    # PETA dataset
    peta_path = dataset_path / "PETA"
    peta_path.mkdir(parents=True, exist_ok=True)
    peta_zipfile = peta_path / "peta.zip"
    print("Download PETA dataset")
    url = "https://www.dropbox.com/s/52ylx522hwbdxz6/PETA.zip?dl=1"
    download_url(url, peta_zipfile)
    print("Extract PETA dataset")
    extract_zip(peta_zipfile, peta_path)
    peta_img_path = peta_path / "images"
    peta_img_path.mkdir(parents=True, exist_ok=True)
    mapping = {row[0]: row[1] for row in np.genfromtxt("peta_file_mapping.txt", dtype=str, delimiter=",")}
    for file in tqdm(peta_path.glob("*/*/*/*")):
        if file.suffix == ".txt":
            continue
        shutil.move(file, dataset_path / mapping[str(PurePosixPath(file)).replace(str(dataset_path) + "/", "")])


def prepare_annotations(dataset_path):
    anno_path = dataset_path #/ "annotations"
    anno_path.mkdir(parents=True, exist_ok=True)
    anno_zipfile = anno_path / "development.zip"
    print("Download annotations")
    url = "https://drive.google.com/file/d/1LeP3i59wJG9QZNwwz4iIyiU9iTCB4yQv/view?usp=sharing"
    gdown.download(url, output=str(anno_zipfile), quiet=False, use_cookies=False, fuzzy=True)
    print("Extract annotations")
    extract_zip(anno_zipfile, anno_path)


def prepare_templates(dataset_path):
    template_zipfile = dataset_path / "submission_templates.zip"
    print("Download templates")
    url = "https://drive.google.com/file/d/1dnciiDxOQcPCvhXCSMFlENAdn7Mfp-ow/view?usp=sharing"
    gdown.download(url, output=str(template_zipfile), quiet=False, use_cookies=False, fuzzy=True)
    print("Extract templates")
    extract_zip(template_zipfile, dataset_path)


def prepare_datasets(path):
    # Datasets folder
    dataset_path = Path(path)
    dataset_path.mkdir(parents=True, exist_ok=True)

    # Download & extract datasets
    prepare_market(dataset_path)
    prepare_pa100k(dataset_path)
    prepare_peta(dataset_path)

    # Download & extract annotations
    prepare_annotations(dataset_path)

    # Download & extract submission templates
    prepare_templates(Path("./"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="WACV2023 RWS UPAR Challenge",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default="./data",
        help="Dataset directory. Downloaded datasets are stored in this directory.",
    )
    args = parser.parse_args()

    prepare_datasets(args.data_dir)
