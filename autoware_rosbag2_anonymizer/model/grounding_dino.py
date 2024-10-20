from groundingdino.util.inference import Model


class GroundingDINO:
    def __init__(self, config_path, checkpoint_path, device) -> None:
        self.model = self.load_model(config_path, checkpoint_path, device)
        self.counter = 0

    def load_model(self, config_path, checkpoint_path, device):
        model = Model(
            model_config_path=config_path,
            model_checkpoint_path=checkpoint_path,
            device=device,
        )
        return model

    def __call__(self, image, classes, box_threshold, text_threshold):
        detections = self.model.predict_with_classes(
            image=image,
            classes=classes,
            box_threshold=box_threshold,
            text_threshold=text_threshold,
        )
        return detections
