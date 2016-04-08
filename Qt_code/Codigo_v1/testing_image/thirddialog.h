#ifndef THIRDDIALOG_H
#define THIRDDIALOG_H

#include <QDialog>

namespace Ui {
class thirdDialog;
}

class thirdDialog : public QDialog
{
    Q_OBJECT

public:
    explicit thirdDialog(QWidget *parent = 0);
    ~thirdDialog();


private:
    Ui::thirdDialog *ui;
    int counter;
    int counter2;


private slots:
    void button_Plus_click();
    void button_Minus_click();
    void button_Plus_click2();
    void button_Minus_click2();
    void on_pushButton_5_clicked();
};
#endif // THIRDDIALOG_H
