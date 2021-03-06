#include "secdialog.h"
#include "ui_secdialog.h"
#include "thirddialog.h"
#include "fourthdialog.h"
#include "fifdialog.h"
#include "monidialog.h"

SecDialog::SecDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SecDialog)
{
    ui->setupUi(this);
    QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
     ui->label->setPixmap(pix);
}

SecDialog::~SecDialog()
{
    delete ui;
}

void SecDialog::on_pushButton_7_clicked()
{
    thirdDialog thirddialog;
    thirddialog.setModal(true);
    thirddialog.exec();
}


void SecDialog::on_pushButton_8_clicked()
{
    fourthDialog fourthdialog;
    fourthdialog.setModal(true);
    fourthdialog.exec();
}

void SecDialog::on_pushButton_6_clicked()
{
    fifDialog fifdialog;
    fifdialog.setModal(true);
    fifdialog.exec();
}

void SecDialog::on_pushButton_4_clicked()
{
    moniDialog monidialog;
    monidialog.setModal(true);
    monidialog.exec();
}
