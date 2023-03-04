class Checker:

    def is_text(self, filename: str):
        return filename.lower().endswith(
            (
                '.txt', '.doc', '.docx',
            )
        )

    def is_audio(self, filename: str):
        return filename.lower().endswith(
            (
                '.mp3', '.flac', '.mid',
                '.wav', '.aif', '.m3u8',
                '.aa3', '.flm', '.ec3',
                '.mtm', '.flp', '.weba',
                '.wproj', '.wow','.vlc',
            )
        )

    def is_image(self, filename: str) -> bool:
        return filename.lower().endswith (
            (
                '.jpeg', '.jpg', '.png',
                '.webp', '.gif', '.tiff',
                '.psd', '.raw', '.ai',
                '.indd', '.eps'
            )
        )

    def is_video(self, filename: str):
        return filename.lower().endswith (
            (
                '.mp4', '.mpg', '.mov',
                '.wmv', '.rm', '.mkv',
                '.webm', '.aep', '.kine',
                '.prproj', '.veg', '.drp',
                '.kdenlive', '.cpvc'
            )
        )

    def is_archive(self, filename: str):
        return filename.lower().endswith(
            (
                '.zip', '.rar', '.gz',
                '.tar', '.7z', '.jar',
                '.djvu', '.zipx', '.tar.gz',
                '.odb', '.bz', '.bz2', '.gzip',
                '.tgz', '.z'
                
            )
        )
