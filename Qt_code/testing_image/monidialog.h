#ifndef MONIDIALOG_H
#define MONIDIALOG_H

#include <QDialog>


namespace Ui {
class moniDialog;
}

class moniDialog : public QDialog
{
    Q_OBJECT

public:
    explicit moniDialog(QWidget *parent = 0);
    ~moniDialog();

private slots:


    void updateLCD_temp(const QString);
    void updateLCD_potencia(const QString);
    void updateLCD_imp(const QString);
    void updateLCD_tempo(const QString);
    void on_pushButton_8_clicked();

private:
    Ui::moniDialog *ui;


};

#endif // MONIDIALOG_H
