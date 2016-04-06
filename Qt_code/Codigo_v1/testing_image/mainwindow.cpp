#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "secdialog.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
   // this->setStyleSheet("background-color: white;");
   QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
    ui->label_2->setPixmap(pix);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
       SecDialog secdialog;
       secdialog.setModal(true);
       secdialog.exec();

}
