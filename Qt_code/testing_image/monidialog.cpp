#include "monidialog.h"
#include "ui_monidialog.h"
//#include <QSerialPort>
//#include <QSerialPortInfo>
#include <string>
#include <QDebug>
#include <QMessageBox>

#include <QTextStream>
#include <QtCore/QString>
#include <QtCore/QFile>
#include <QtCore/QTextStream>
//#include <thiddialog.h>

moniDialog::moniDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::moniDialog)
{
    ui->setupUi(this);
  //  QPixmap pix("/home/pedro/Desktop/Teste3_interface/imagens/logo.png");

  QPixmap pix("/home/pi/Desktop/Teste2_interface/imagens/logo.png");
    ui->label->setPixmap(pix);
   // this ->ui->lcdNumber_10->display(233);    //variavel de potencia
    //this ->ui->lcdNumber_8->display(233);    //variavel de temperatura
   // this ->ui->lcdNumber_9->display(233);   //variavel de impedancia
   // this ->ui->lcdNumber_7->display(233);   //variavel de tempo

QString line;
    QString filename = "/home/pi/Desktop/potencia.txt";
        QFile file(filename);
        if (file.open(QIODevice::ReadWrite)) {
            QTextStream stream(&file);
            line = stream.readLine();
            qDebug() << line;
        }


 this ->ui->lcd_potencia->display(line);   //variavel de tempo
    //  moniDialog::updateLCD_potencia(line);
       moniDialog::updateLCD_temp("30");
        moniDialog::updateLCD_tempo("---");
         moniDialog::updateLCD_imp("50");
 file.close();
}


moniDialog::~moniDialog()
{

    delete ui;
}


void moniDialog::updateLCD_potencia(const QString sensor_reading){

    ui->lcd_potencia->display(sensor_reading);    //variavel de potencia


}
void moniDialog::updateLCD_imp(const QString sensor_reading){

    ui->lcd_imp->display(sensor_reading);    //variavel de impedancia


}

void moniDialog::updateLCD_tempo(const QString sensor_reading){

    ui->lcd_tempo->display(sensor_reading);    //variavel de tempo

}

void moniDialog::updateLCD_temp(const QString sensor_reading){

    ui->lcd_temp->display(sensor_reading);    //variavel de temp

}

void moniDialog::on_pushButton_8_clicked()
{
    QString filename ="/home/pi/Desktop/potencia.txt";
    QFile file(filename);
   // if (file.open(QIODevice::ReadWrite)) {
     //   QTextStream stream(&file);
       // stream << "100" << endl;
         //   }
    //file.close();
    if (file.open(QIODevice::ReadWrite)) {
        QTextStream stream(&file);
        stream << "100" << endl;
	
            }
file.close();

  // if (file.open(QIODevice::ReadWrite)) {
    //    QTextStream stream(&file);
      //  stream << "0" << endl;

        //    }
//file.close();

}
