# This Python file uses the following encoding: utf-8
import sys
import matplotlib
import random
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6 import QtCore

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from Heater import Heater, PID

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    setpoint = 30
    dt = 0.2
    current_time = 0;
    Heater1_maxpower = 10000;

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.set_ylim(0, 110)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.ui.verticalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)

        self.heater = Heater()
        self.pid = PID(maxpower=self.Heater1_maxpower)

        self.ui.param_C_edit.setText(str(self.heater.C_air))
        self.ui.param_L_edit.setText(str(self.heater.L_air))
        self.ui.param_Ro_edit.setText(str(self.heater.Ro_air))
        self.ui.param_T_edit.setText(str(self.heater.temp_air))
        self.ui.pid_I_edit.setText(str(self.pid.ki))
        self.ui.pid_P_edit.setText(str(self.pid.kp))
        self.ui.pid_D_edit.setText(str(self.pid.kd))
        self.ui.pid_setPoint_edit.setText(str(self.setpoint))

        self.ui.param_Heater1_power.setText(str(self.Heater1_maxpower))

        n_data = 500
        self.xdata = list(range(n_data))

        self.temp_y_data = list()
        self.power_y_data = list()

        for i in range(n_data):
            self.temp_y_data.append(0)
            self.power_y_data.append(0)

        self._plot_ref = list()
        self.update_plot()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.ui.param_C_edit.editingFinished.connect(self.update_param)
        self.ui.param_L_edit.editingFinished.connect(self.update_param)
        self.ui.param_Ro_edit.editingFinished.connect(self.update_param)
        self.ui.param_T_edit.editingFinished.connect(self.update_param)

        self.ui.param_Heater1_power.editingFinished.connect(self.update_param)

        self.ui.pid_D_edit.editingFinished.connect(self.update_param)
        self.ui.pid_I_edit.editingFinished.connect(self.update_param)
        self.ui.pid_P_edit.editingFinished.connect(self.update_param)
        self.ui.pid_setPoint_edit.editingFinished.connect(self.update_param)


    def update_plot(self):
        temp, time = self.compute()

        self.temp_y_data = self.temp_y_data[1:] + [temp]
        self.power_y_data = self.power_y_data[1:] + [self.heater.power / self.Heater1_maxpower * 100]

        # Note: we no longer need to clear the axis.
        if len(self._plot_ref) ==0:
            self._plot_ref.append(self.canvas.axes.plot(self.xdata, self.temp_y_data, 'r', color='green')[0])
            self._plot_ref.append(self.canvas.axes.plot(self.xdata, self.power_y_data, 'r', color='red')[0])
        else:
            self._plot_ref[0].set_ydata(self.temp_y_data)
            self._plot_ref[1].set_ydata(self.power_y_data)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    def update_param(self):
        self.heater.L_air = float(self.ui.param_L_edit.text())
        self.heater.Ro_air = float(self.ui.param_Ro_edit.text())
        self.heater.temp_air = float(self.ui.param_T_edit.text())
        self.heater.C_air = float(self.ui.param_C_edit.text())

        Heater1_maxpower = float(self.ui.param_Heater1_power.text())

        self.pid.ki = float(self.ui.pid_I_edit.text())
        self.pid.kp = float(self.ui.pid_P_edit.text())
        self.pid.kd = float(self.ui.pid_D_edit.text())
        self.setpoint = int(self.ui.pid_setPoint_edit.text())

    def compute(self):
        value = self.pid.computePID(self.heater.current_temp_air, self.setpoint, self.dt)
        self.heater.compute(value, self.dt)
        return self.heater.current_temp_air, self.heater.power


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
