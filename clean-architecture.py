#!/usr/bin/env python3
import os


class CleanArchitecture:
    default_project_directory = os.getcwd()
    feature_name = ""
    is_tdd = False
    base_dir = ""
    test_dir = ""
    feature_folder_name = ""

    def get_dir_to_make(self, base_dir, is_tdd, test_dir):
        dir_list = []

        dir_list.append("{}/data/datasource".format(base_dir))
        dir_list.append("{}/data/models".format(base_dir))
        dir_list.append("{}/data/repositories".format(base_dir))

        dir_list.append("{}/domain/entities".format(base_dir))
        dir_list.append("{}/domain/repositories".format(base_dir))

        dir_list.append("{}/presentation/bloc".format(base_dir))
        dir_list.append("{}/presentation/pages".format(base_dir))
        dir_list.append("{}/presentation/widgets".format(base_dir))

        if is_tdd:
            dir_list.append("{}/data/datasource".format(test_dir))
            dir_list.append("{}/data/models".format(test_dir))
            dir_list.append("{}/data/repositories".format(test_dir))

            dir_list.append("{}/domain/entities".format(test_dir))
            dir_list.append("{}/domain/repositories".format(test_dir))
            dir_list.append("{}/domain/usecases".format(test_dir))
            dir_list.append("{}/domain/usecases".format(base_dir))

            dir_list.append("{}/presentation/bloc".format(test_dir))
            dir_list.append("{}/presentation/pages".format(test_dir))
            dir_list.append("{}/presentation/widgets".format(test_dir))

        return dir_list

    def make_directories(
        self, feature_name, directory, is_tdd_enable, feature_folder_name
    ):
        self.feature_folder_name = feature_folder_name
        if directory:
            self.default_project_directory = directory

        if feature_name:
            self.feature_name = feature_name

        self.is_tdd = is_tdd_enable

        self.base_dir = (
            self.default_project_directory
            + "/lib/{}/".format(self.feature_folder_name)
            + self.feature_name
        )

        if self.is_tdd:
            self.test_dir = (
                self.default_project_directory
                + "/test/{}/".format(self.feature_folder_name)
                + self.feature_name
            )

        dir_to_make_list = self.get_dir_to_make(
            self.base_dir, self.is_tdd, self.test_dir
        )

        for dir in dir_to_make_list:
            print("Directory : {}".format(dir))
            os.system("mkdir -p {}".format(dir))


def is_tdd_enable_value(prompt):
    while True:
        try:
            return {"true": True, "false": False}[
                input(prompt).lower().strip() or "false"
            ]
        except KeyError:
            print("Invalid input. Please enter True or False")


def is_feature_empty():
    while True:
        feature = input("Enter feature (counter, auth, etc) : ")
        if feature.strip():
            return feature


if __name__ == "__main__":
    user_input_directory = input(
        "Enter project directory (If not provided, current working directory will be used) : "
    )

    feature_folder_name = (
        input(
            "Enter feature folder name or reletive path also could be used i.e. ui/feature (default feature will be used) : "
        )
        or "feature"
    )

    feature_name = is_feature_empty()

    is_tdd_enable = is_tdd_enable_value("Enter TDD (True, False defaut: False) : ")

    clean_arch = CleanArchitecture()
    clean_arch.make_directories(
        feature_name=feature_name,
        directory=user_input_directory,
        is_tdd_enable=is_tdd_enable,
        feature_folder_name=feature_folder_name,
    )
