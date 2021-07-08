def download_dir(remote_dir, local_dir):
    import os

    os.path.exists(local_dir) or os.makedirs(local_dir)
    dir_items = sftp.listdir_attr(remote_dir)
    for item in dir_items:
        # assuming the local system is Windows and the remote system is Linux
        # os.path.join won't help here, so construct remote_path manually
        remote_path = remote_dir + "/" + item.filename
        local_path = os.path.join(local_dir, item.filename)
        if S_ISDIR(item.st_mode):
            download_dir(remote_path, local_path)
        else:
            sftp.get(remote_path, local_path)


download_dir(
    "~/bioinfo-lecture-2021-07/0708/",
    "\\Users\\vin\\Downloads\\sequence.fasta",
)


with open("sequence.protein.fasta", "r") as handle:
    handle.wirte(sequence.fasta)
