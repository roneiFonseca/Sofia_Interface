#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void on_pushButton_menos_clicked();

    void on_pushButton_mais_clicked();

private:
    Ui::MainWindow *ui;
    int counter;

};

#endif // MAINWINDOW_H
