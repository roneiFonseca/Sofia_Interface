/********************************************************************************
** Form generated from reading UI file 'thirddialog.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_THIRDDIALOG_H
#define UI_THIRDDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_thirdDialog
{
public:
    QLabel *label;
    QLabel *label_2;
    QLCDNumber *lcdNumber;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QLabel *label_3;
    QPushButton *pushButton_3;
    QLabel *label_4;
    QLCDNumber *lcdNumber_2;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QLabel *label_8;
    QLabel *label_9;

    void setupUi(QDialog *thirdDialog)
    {
        if (thirdDialog->objectName().isEmpty())
            thirdDialog->setObjectName(QStringLiteral("thirdDialog"));
        thirdDialog->resize(634, 446);
        thirdDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label = new QLabel(thirdDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../untitled/imagens/teste.JPG")));
        label_2 = new QLabel(thirdDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(150, 130, 301, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        lcdNumber = new QLCDNumber(thirdDialog);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        lcdNumber->setGeometry(QRect(40, 270, 71, 51));
        pushButton = new QPushButton(thirdDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(170, 240, 51, 41));
        pushButton_2 = new QPushButton(thirdDialog);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(170, 290, 51, 41));
        label_3 = new QLabel(thirdDialog);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(80, 210, 91, 21));
        label_3->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_3->setAlignment(Qt::AlignCenter);
        pushButton_3 = new QPushButton(thirdDialog);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(520, 240, 51, 41));
        label_4 = new QLabel(thirdDialog);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(430, 210, 91, 21));
        label_4->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_4->setAlignment(Qt::AlignCenter);
        lcdNumber_2 = new QLCDNumber(thirdDialog);
        lcdNumber_2->setObjectName(QStringLiteral("lcdNumber_2"));
        lcdNumber_2->setGeometry(QRect(390, 270, 71, 51));
        pushButton_4 = new QPushButton(thirdDialog);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(520, 290, 51, 41));
        pushButton_5 = new QPushButton(thirdDialog);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(510, 370, 75, 23));
        label_8 = new QLabel(thirdDialog);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(120, 310, 47, 13));
        label_8->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_9 = new QLabel(thirdDialog);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(470, 310, 47, 13));
        label_9->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));

        retranslateUi(thirdDialog);
        QObject::connect(pushButton_5, SIGNAL(clicked()), thirdDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(thirdDialog);
    } // setupUi

    void retranslateUi(QDialog *thirdDialog)
    {
        thirdDialog->setWindowTitle(QApplication::translate("thirdDialog", "Dialog", 0));
        label->setText(QString());
        label_2->setText(QApplication::translate("thirdDialog", "POT\303\212NCIA ", 0));
        pushButton->setText(QApplication::translate("thirdDialog", "+", 0));
        pushButton_2->setText(QApplication::translate("thirdDialog", "-", 0));
        label_3->setText(QApplication::translate("thirdDialog", "Inicial", 0));
        pushButton_3->setText(QApplication::translate("thirdDialog", "+", 0));
        label_4->setText(QApplication::translate("thirdDialog", "Final", 0));
        pushButton_4->setText(QApplication::translate("thirdDialog", "-", 0));
        pushButton_5->setText(QApplication::translate("thirdDialog", "OK", 0));
        label_8->setText(QApplication::translate("thirdDialog", "W", 0));
        label_9->setText(QApplication::translate("thirdDialog", "W", 0));
    } // retranslateUi

};

namespace Ui {
    class thirdDialog: public Ui_thirdDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_THIRDDIALOG_H
