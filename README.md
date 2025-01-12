# SemEval-2025 Task 10 / Projekt R
Task description

## Usage

### Current best solution(1st subtask)
##### Determining the main class - Antagonist/Protagonist/Innocent

[using XLM-Roberta and adding special span tokens](solutions/custom_tokens/xlm-roberta-span-tokens.ipynb)

[using XLM-Roberta adding special span tokens - deciding the class from start_span token embedding](solutions/custom_tokens/xlm_roberta_with_classification_on_start_span_token.ipynb)

##### Determining fine-grained roles

[Local classifier per parent node](solutions/hierarchical_classification/LCPN_with_metrics_only_classifier_withoutMLP.ipynb)


#### Folder organisation:
- data/
    - contains dev_set, scorers_baselines and train_data
    - all data is categorized by languages
- merged_data/
    - contains data that is directly used in our programs
- PreProcess_and_EDA/
    - contains scripts to merge, translate and organise data for usage
    - exploratory data analysis in EDA files
- solutions/
    -subtask1/
        - contains our solutions for the first subtask



## License
Add licensing information here
