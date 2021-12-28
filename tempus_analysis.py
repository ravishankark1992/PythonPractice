import json
from argparse import ArgumentParser
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.gaussian_process import GaussianProcessClassifier
# from sklearn.datasets import load_iris
from pandas import DataFrame
from sklearn.gaussian_process.kernels import RBF
from sklearn.model_selection import train_test_split


# X, y = load_iris(return_X_y=True)


def load_json_file(file_path):
    f = open(file_path)
    json_data = json.load(f)
    return json_data


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer


def get_gender(gender_label):
    le = LabelEncoder()
    gender = 0
    return gender


def main():
    patient_profiles_file_path = "C:\\Users\\ravis\\Downloads\\tempus_data_science_case_study\\patient_profiles.json"
    biomarkers_file_path = "C:\\Users\\ravis\\Downloads\\tempus_data_science_case_study\\biomarkers.csv"
    targets_file_path = "C:\\Users\\ravis\\Downloads\\tempus_data_science_case_study\\targets.csv"

    patient_profiles_data = load_json_file(patient_profiles_file_path)
    # biomarkers_data = pd.read_csv(biomarkers_file_path)
    targets_data = pd.read_csv(targets_file_path)
    age_dict = {}
    gender_dict = {}
    race_dict = {}
    disease_sub_type_dict = {}
    comorbidity_index_dict = {}
    cohort_qualifier_dict = {}
    smoking_status_dict = {}
    months_since_diagnosis_dict = {}
    model_input_data = []
    model_target = []
    missing_counter = 0

    for institution_detail in patient_profiles_data:
        for patient in institution_detail["patient_profiles"]:
            try:
                target_row = targets_data.loc[targets_data["patient_id"] == patient["patient_id"]]
                if not target_row.empty:
                    model_target.append(target_row.target_label.values[0])

                else:
                    missing_counter += 1
                    continue
            except:
                print("failed")
                continue

            age_dict[patient["patient_id"]] = patient["demographics"].get("age")
            gender_dict[patient["patient_id"]] = patient["demographics"].get("gender")
            race_dict[patient["patient_id"]] = patient["demographics"].get("race")
            disease_sub_type_dict[patient["patient_id"]] = patient["status"].get("disease_sub_type")
            comorbidity_index_dict[patient["patient_id"]] = patient["status"].get("comorbidity_index")
            cohort_qualifier_dict[patient["patient_id"]] = patient["status"].get("cohort_qualifier")
            smoking_status_dict[patient["patient_id"]] = patient["status"].get("smoking_status")
            months_since_diagnosis_dict[patient["patient_id"]] = patient["status"].get("months_since_diagnosis")

            row = [
                patient["patient_id"],
                patient["demographics"].get("age"),
                patient["demographics"].get("gender"),
                patient["demographics"].get("race"),
                patient["status"].get("disease_sub_type"),
                patient["status"].get("comorbidity_index"),
                patient["status"].get("cohort_qualifier"),
                patient["status"].get("smoking_status"),
                patient["status"].get("months_since_diagnosis")
            ]

            model_input_data.append(row)
    model_input_data = np.array(model_input_data)
    patient_info = pd.DataFrame(model_input_data[:, 1:], columns=[  # 'patient_id',
        'age',
        'gender',
        'race',
        'disease_sub_type',
        'comorbidity_index',
        'cohort_qualifier',
        'smoking_status',
        'months_since_diagnosis'],
                                )
    col_trans = make_column_transformer((OneHotEncoder(), [
                                                           'gender',
                                                           'race',
                                                           'disease_sub_type',
                                                           'cohort_qualifier',
                                                           'smoking_status',
                                                           ]),
                                        remainder='passthrough')
    encoded_patient_info = col_trans.fit_transform(patient_info)
    print('training')
    X_train, X_test, y_train, y_test = train_test_split(encoded_patient_info, model_target, test_size=0.73,

                                                        random_state=42)
    kernel = 1.0 * RBF(1.0)
    gpc = GaussianProcessClassifier(kernel=kernel, random_state=0).fit(X_train, y_train)
    print(gpc.predict_proba(X_test[:10, :]))
    print('training data size', len(model_target))
    print('missing_counter', missing_counter)
    print(len(age_dict))



main()


"""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit()
"""