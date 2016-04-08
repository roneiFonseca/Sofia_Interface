#ifndef FOURTHDIALOG_H
#define FOURTHDIALOG_H

#include <QDialog>

namespace Ui {
class fourthDialog;
}

class fourthDialog : public QDialog
{
    Q_OBJECT

public:
    explicit fourthDialog(QWidget *parent = 0);
    ~fourthDialog();

private:
    Ui::fourthDialog *ui;
    int counter3;
    int counter4;


private slots:
    void button_Plus_click3();
    void button_Minus_click3();
    void button_Plus_click4();
    void button_Minus_click4();
};
#endif // FOURTHDIALOG_H
