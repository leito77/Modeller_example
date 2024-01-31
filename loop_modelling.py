from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = environ()

# directories for input atom files
#env.io.atom_files_directory = ['.', '../atom_files']

class MyModel(automodel):
    def select_atoms(self):
        return selection(self.residue_range('174:A', '185:A'))
        return selection(self.residue_range('224:A', '225:A'))
        return selection(self.residue_range('230:A', '233:A'))
        return selection(self.residue_range('292:A', '315:A'))
        return selection(self.residue_range('325:A', '325:A'))
        return selection(self.residue_range('329:A', '329:A'))
        return selection(self.residue_range('337:A', '337:A'))
        return selection(self.residue_range('363:A', '365:A'))
        return selection(self.residue_range('367:A', '366:A'))
        return selection(self.residue_range('370:A', '375:A'))
        return selection(self.residue_range('397:A', '413:A'))
        return selection(self.residue_range('445:A', '451:A'))
        return selection(self.residue_range('479:A', '480:A'))
        return selection(self.residue_range('496:A', '521:A'))
        return selection(self.residue_range('841:A', '486:A'))
        return selection(self.residue_range('319:A', '927:A'))

a = MyModel(env, alnfile = 'alignment.ali',
            knowns = '5is5', sequence = '5is5_fill')
a.starting_model= 1
a.ending_model  = 1

a.make()
