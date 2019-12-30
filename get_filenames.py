from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from os.path import basename

def get_filenames():
    """
    get filenames with graphical interface
        
    Returns
    -------
    file_list : list
        list of chosen filenames
    """
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_list=askopenfilenames()
    return file_list


def get_fps_from_fname(file):
    """Get fps from filename with stamp '_1000fps', where 1000 is fps value.
        
        Parameters
        ----------
        file : str 
            filename with full path
        
        Returns:
        -------
        fps: int
            fps of videofile (frames/second) """
            
    filename = basename(file)
    i = filename.find('fps')
    j=i
    while filename[j] != '_':
        j = j-1
    fps=int(filename[j+1:i])
    return fps