from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits PyDataProcess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def get_process_factory(self):
        # Instantiate algorithm object
        from train_yolo_v11.train_yolo_v11_process import TrainYoloV11Factory
        return TrainYoloV11Factory()

    def get_widget_factory(self):
        # Instantiate associated widget object
        from train_yolo_v11.train_yolo_v11_widget import TrainYoloV11WidgetFactory
        return TrainYoloV11WidgetFactory()
