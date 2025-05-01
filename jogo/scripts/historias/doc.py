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

def get_documents_folder():
    FOLDERID_Documents = string_to_guid('FDD39AD0-238F-46AF-ADB4-6C85480369C7')

    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)]
    SHGetKnownFolderPath.restype = ctypes.HRESULT

    path_ptr = ctypes.c_wchar_p()
    result = SHGetKnownFolderPath(ctypes.byref(FOLDERID_Documents), 0, None, ctypes.byref(path_ptr))

    if result != 0:
        raise OSError(f"Erro ao obter o caminho da pasta 'Documentos': {result}")

    return path_ptr.value


if __name__ == '__main__':
    print(f"A pasta Documentos está em: {get_documents_folder()}")

shutil.copy("quest/parte1.py", f"{get_documents_folder()}")
