import stat
from paramiko import Transport
from paramiko.sftp_client import SFTPClient


def main():
    t = Transport(('127.0.0.1', 2222))
    t.connect(None, 'foo', 'pass')

    sftp = SFTPClient.from_transport(t)
    loc = 'upload'
    items_1 = []
    items_2 = []
    files = []
    for item in sftp.listdir(loc):
        items_1.append(item)
    for item in sftp.listdir_iter(loc):
        items_2.append(item.filename)
        if stat.S_IFMT(item.st_mode) != stat.S_IFDIR:
            files.append(item)
    assert items_1 == items_2
    print(f'{len(items_2)} items listed but only {len(files)} files')


if __name__ == '__main__':
    main()
