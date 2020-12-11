import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AlPR1UP4hr5mBFve54VED84WakBEedQZpeRdUp0BBHh0gEtrkdYOG6jAYklt4mtWivwNM_PXT2qXHspGBkNLgA4IWbjG6aJ0c7mliN-hLwFDjmR4t-Mxu1-1wEbsQBZVe5vB5NM'
    transferData = TransferData(access_token)

    file_from = input('path from')
    file_to = input('path to')
    # API v2
    transferData.upload_file(file_from, file_to)
    print('success')

if __name__ == '__main__':
    main()