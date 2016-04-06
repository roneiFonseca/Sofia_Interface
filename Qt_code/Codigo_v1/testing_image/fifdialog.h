#ifndef FIFDIALOG_H
#define FIFDIALOG_H

#include <QDialog>

namespace Ui {
class fifDialog;
}

class fifDialog : public QDialog
{
    Q_OBJECT

public:
    explicit fifDialog(QWidget *parent = 0);
    ~fifDialog();

private:
    Ui::fifDialog *ui;
};

#endif // FIFDIALOG_H
