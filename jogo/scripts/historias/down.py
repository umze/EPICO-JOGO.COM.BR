import ctypes
from ctypes import windll, wintypes
import shutil

class GUID(ctypes.Structure):
    _fields_ = [
        ('Data1', ctypes.c_ulong),
        ('Data2', ctypes.c_ushort),
        ('Data3', ctypes.c_ushort),
        ('Data4', ctypes.c_ubyte * 8)
    ]

def string_to_guid(guid_string):
    import uuid
    u = uuid.UUID(guid_string)
    data4 = (ctypes.c_ubyte * 8)(*u.bytes[8:])
    return GUID(u.fields[0], u.fields[1], u.fields[2], data4)

def get_downloads_folder():
    FOLDERID_Downloads = string_to_guid('374DE290-123F-4565-9164-39C4925E467B')
    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)]
    SHGetKnownFolderPath.restype = ctypes.HRESULT

    path_ptr = ctypes.c_wchar_p()
    result = SHGetKnownFolderPath(ctypes.byref(FOLDERID_Downloads), 0, None, ctypes.byref(path_ptr))

    if result != 0:
        raise OSError(f"Erro ao obter o caminho da pasta 'Downloads': {result}")

    return path_ptr.value

if __name__ == '__main__':
    print(f"A pasta Downloads tá em: {get_downloads_folder()}")

shutil.copy("quest/parte2.py", f"{get_downloads_folder()}")
