"""Django zip stream responses."""
from django.http import HttpResponse


class TransferZipResponse(HttpResponse):
    """A streaming zip HttpResponse.

    :param filename: Name of the zip file to be used.
    :param files: list of (path, system_path, size) tuples to be zipped


    Usage::

      >>> files = [
          ("/chicago.jpg", "/home/travis/chicago.jpg", 4096),
          ("/portland.jpg", "/home/travis/portland.jpg", 4096),
      ]
      >>> TransferZipResponse(filename='download.zip', files=files)
    """

    def __init__(self, filename, files):
        """
        Parameters
        filename (string) - Name of the zip file to be streamed.
        files (list of (path, system_path, size) tuples) - List of files to
            be transferred.
        """

        content = "\n".join(
            [self._build_content(file_info) for file_info in files])

        super(TransferZipResponse, self).__init__(
            content, status=200, content_type="application/zip")

        self["X-Archive-Files"] = 'zip'
        self['Content-Disposition'] = (
            'attachment; filename="{}"'.format(filename))

    @staticmethod
    def _build_content(file_info):
        """Return the content string body of a single file for use upstream.

        Given a file_info tuple (path, system_path, size), this method
        assembles a string containing mod_zip commands for a single file.
        """
        path, system_path, size = file_info
        single_file_info = "- %s %s %s" % (size, system_path, path)
        return single_file_info
