# -*- coding: utf-8 -*-
import os
def record_to_csv(data, save_path):
    '''
    '''

    recorded_list = []
    for type in ['CYST', 'FNH', 'HCC', 'HEM', 'METS']:
        slice_names = os.listdir(os.path.join(dataset_dir, type))
        for slice_name in slice_names:
            if '_' in slice_name:
                recorded_list.append(slice_name)
    import csv
    with open(save_path, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(recorded_list)