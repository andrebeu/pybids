import os

class bidspaths(object):

    def __init__(self, basedir):
        """
        Parameters
        ----------
        basedir : path
          Path to the dataset (i.e. the directory with the 'sub-*'
          subdirectories).
        """
        self.basedir = os.path.expanduser(os.path.expandvars(basedir))

    def get_subj_foldernames(self):
        """Return a (sorted) list of IDs for all subjects in the dataset

        Standard numerical subject IDs a returned as integer values. All other
        types of IDs are returned as strings with the 'sub' prefix stripped.
        """

        subj_ids = []
        for fil in os.listdir(self.basedir):
            if fil.startswith('sub-'):
                subj_ids.append(fil)
        return subj_ids


    def get_bold_run_filenames(self, subj, ses, task):
        sub=self.get_subj_ids()[subj-1]
        ses='ses-'+ses
        task='task-'+task
        bolds=[]
        for fil in os.listdir(_opj(self.basedir,sub,ses,'func')):
            if fil.endswith('bold.nii') or fil.endswith('bold.nii.gz'):
                bolds.append(fil)
        return bolds        


    def get_task_bold_run_filenames(self, ses, task):
        """Return a dictionary with run IDs by subjects for a given task

        Dictionary keys are subject IDs, values are lists of run IDs.
        """
        out = {}
        for sub in range(len(self.get_subj_ids())):
            runs = self.get_bold_run_ids(sub, ses, task)
            if len(runs):
                out[sub+1] = runs
        return out
        

# basedir = '/Users/andrebeukers/Documents/fMRI/Python/Study Forrest/video_studyforrest'
# bids = bidsDataset(basedir)
# bids.get_subj_foldernames
# bids.get_bold_run_filenames(1,ses='movie',task='movie')
# bids.get_task_bold_run_filenames(ses='movie',task='movie')