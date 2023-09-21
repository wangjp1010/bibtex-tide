rules = {
    # 'replacement': ['pattern1', 'pattern2', ...]
    r"{NAACL}": [r".*North American Chapter of the Association for Computational Linguistics.*"],
    r"{WMT}": [r".*Conference on Machine Translation.*"],
    r"{OSDI}": [r"Proceedings of the.*Conference on Operating Systems Design and Implementation.*"],
    r"{NeurIPS}": [r".*Neural Information Processing Systems.*"],
    r"{ICML}": [r".*International Conference on Machine Learning.*"],
    r"{ACL}": [r".*Meeting of the Association for Computational Linguistics.*", ".*Proceedings of the.*Conference of the Association for Computational Linguistics.*"],
    r"{EMNLP}": [r"Proceedings of the.*Conference on Empirical Methods in Natural Language Processing.*"],
    r"{ICLR}": [r".*International Conference on Learning Representations.*"],
    r"{COLING}": [r"Proceedings of the.*International Conference on Computational Linguistics.*"],
    r"{EACL}": [r"Proceedings of the.*Conference of the European Chapter of the Association for Computational Linguistics.*"],
    r"{IJCAI}": [r"Proceedings of the International Joint Conference on Artificial Intelligence.*"],
    r"{AAAI}": [r".*Conference on Artificial Intelligence.*"],
    r"{ICCV}": [r".*International Conference on Computer Vision.*"],
    r"{CVPR}": [r"Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.*"],
    r"{ICRA}": [r"Proceedings of the IEEE International Conference on Robotics and Automation.*"],
    r"{KDD}": [r".*International Conference on Knowledge Discovery.*"],
    r"{CVSC}": [r".*Continuous Vector Space Models and their Compositionality.*"],
    r"{WISA}": [r".*Web Information Systems and Applications.*"],
    r"{INTERSPEECH}": [r".*Conference of the International Speech Communication Association.*"],
    r"{ICDM}": [r".*International Conference on Data Mining.*"],
    r"{CICM}": [r".*Intelligent Computer Mathematics.*"],
    r"{ICPP}": [r".*International Conference on Parallel Processing.*"],

}

keep_keys = ['title', 'author', 'year', 'booktitle', 'journal', 'volume']