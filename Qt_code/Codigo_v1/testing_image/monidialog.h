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

private:
    Ui::moniDialog *ui;
};

#endif // MONIDIALOG_H
