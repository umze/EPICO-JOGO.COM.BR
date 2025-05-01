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

def get_desktop_folder():
    FOLDERID_Desktop = string_to_guid('B4BFCC3A-DB2C-424C-B029-7FE99A87C641')
    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)]
    SHGetKnownFolderPath.restype = ctypes.HRESULT

    path_ptr = ctypes.c_wchar_p()
    result = SHGetKnownFolderPath(ctypes.byref(FOLDERID_Desktop), 0, None, ctypes.byref(path_ptr))

    if result != 0:
        raise OSError(f"Erro ao obter o caminho da Área de Trabalho: {result}")

    return path_ptr.value

# Teste
if __name__ == '__main__':
    print(f"A Área de Trabalho tá em: {get_desktop_folder()}")

shutil.copy("quest/parte3.py", f"{get_desktop_folder()}")
