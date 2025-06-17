/******************************************************************************
*
* Copyright (C) 2009 - 2014 Xilinx, Inc.  All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* Use of the Software is limited solely to applications:
* (a) running on a Xilinx device, or
* (b) that interact with a Xilinx device through a bus or interconnect.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* XILINX  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
* OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
*
* Except as contained in this notice, the name of the Xilinx shall not be used
* in advertising or otherwise to promote the sale, use or other dealings in
* this Software without prior written authorization from Xilinx.
*
******************************************************************************/

/*
 * helloworld.c: simple test application
 *
 * This application configures UART 16550 to baud rate 9600.
 * PS7 UART (Zynq) is not initialized by this application, since
 * bootrom/bsp configures it to baud rate 115200
 *
 * ------------------------------------------------
 * | UART TYPE   BAUD RATE                        |
 * ------------------------------------------------
 *   uartns550   9600
 *   uartlite    Configurable only in HW design
 *   ps7_uart    115200 (configured by bootrom/bsp)
 */

#include <stdio.h>
#include "platform.h"
#include "xil_printf.h"
#include "xparameters.h"
#include "xstatus.h"
#include <xuartlite_l.h>
#include <xil_io.h>
#include <sleep.h>
#include "CPU_IP.h"

#define rst_n            0x00
#define in_1             0x04
#define in_2             0x08
#define out              0x0c
#define out_of           0x10

#define printf           xil_printf

#define uartRegAddr      0x40600000 //addr_UART to communicate with keyboard


uint32_t Display_OUT()
{
    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    return CPU_IP_mReadReg  (baseaddr, out); //CPU_IP_mReadReg (base_addr_IP, offset_slv_reg)
}


void Load_IN(uint32_t offset_input, uint32_t data_input)
{
    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    CPU_IP_mWriteReg (baseaddr, offset_input, data_input); //CPU_IP_mWriteReg (base_addr_IP, offset_slv_reg, data_input)
}

void Rd_Data(char type, uint8_t reg, uint32_t addr_mem)
{
    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    //CPU_IP_mWriteReg (baseaddr, addr_rd_d_mem , addr_mem);
    //CPU_IP_mWriteReg (baseaddr, en_rd_d_mem, 0x1);

    //printf("%c%d = %x\n", type, reg, CPU_IP_mReadReg  (baseaddr, data_rd_d_mem));

    //CPU_IP_mWriteReg (baseaddr, en_rd_d_mem, 0x0);
}
/*
void En_CPU (uint32_t time, uint32_t delay)
{
    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    for (int i=0; i<time; i=i+1)
    {
        CPU_IP_mWriteReg (baseaddr, en_CPU, 0x1);
        usleep(delay); //usleep(delay_number): ham delay
        CPU_IP_mWriteReg (baseaddr, en_CPU, 0x0);
        usleep(delay);
		printf("\nPC = %d\r\n", Display_PC());
        printf("Inst: %x\r\n", Display_Inst());
    }
}
*/
void Rst_IP ()
{
    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    CPU_IP_mWriteReg (baseaddr, rst_n, 0x0);
    CPU_IP_mWriteReg (baseaddr, rst_n, 0x1);
}
/*
void Display_Int_Reg(uint32_t *addr_inst, int from_reg, int to_reg)
{
    //write D-Mem
    for(int i=from_reg; i<=to_reg; i=i+1)
    {
           switch(i)
           {
               case 1:
               {
                   Load_Inst(addr_inst, 0x2a102e23);//2a102e23
                   break;
               }
               case 2:
               {
                   Load_Inst(addr_inst, 0x2c202023);//5e202023
                   break;
               }
               case 3:
               {
                   Load_Inst(addr_inst, 0x2c302223);//5e302223
                   break;
               }
               case 4:
               {
                   Load_Inst(addr_inst, 0x2c402423);//5e402423
                   break;
               }
               case 5:
               {
                   Load_Inst(addr_inst, 0x2c502623);//5e502623
                   break;
               }
               case 6:
               {
                   Load_Inst(addr_inst, 0x2c602823);//5e602823
                   break;
               }
               case 7:
               {
                   Load_Inst(addr_inst, 0x2c702a23);//5e702a23
                   break;
               }
               case 8:
               {
                   Load_Inst(addr_inst, 0x2c802c23);//5e802c23
                   break;
               }
               case 9:
               {
                   Load_Inst(addr_inst, 0x2c902e23);//5e902e23
                   break;
               }
               case 10:
               {
                   Load_Inst(addr_inst, 0x2ea02023);//60a02023
                   break;
               }
               case 11:
               {
                   Load_Inst(addr_inst, 0x2eb02223);//60b02223
                   break;
               }
               case 12:
               {
                   Load_Inst(addr_inst, 0x2ec02423);//60c02423
                   break;
               }
               case 13:
               {
                   Load_Inst(addr_inst, 0x2ed02623);//60d02623
                   break;
               }
               case 14:
               {
                   Load_Inst(addr_inst, 0x2ee02823);//60e02823
                   break;
               }
               case 15:
               {
                   Load_Inst(addr_inst, 0x2ef02a23);//60f02a23
                   break;
               }
               case 16:
               {
                   Load_Inst(addr_inst, 0x2f002c23);//61002c23
                   break;
               }
               case 17:
               {
                   Load_Inst(addr_inst, 0x2f102e23);//61102e23
                   break;
               }
               case 18:
               {
                   Load_Inst(addr_inst, 0x31202023);//63202023
                   break;
               }
               case 19:
               {
                   Load_Inst(addr_inst, 0x31302223);//63302223
                   break;
               }
               case 20:
               {
                   Load_Inst(addr_inst, 0x31402423);//63402423
                   break;
               }
               case 21:
               {
                   Load_Inst(addr_inst, 0x31502623);//63502623
                   break;
               }
               case 22:
               {
                   Load_Inst(addr_inst, 0x31602823);//63602823
                   break;
               }
               case 23:
               {
                   Load_Inst(addr_inst, 0x31702a23);//63702a23
                   break;
               }
               case 24:
               {
                   Load_Inst(addr_inst, 0x31802c23);//63802c23
                   break;
               }
               case 25:
               {
                   Load_Inst(addr_inst, 0x31902e23);//63902e23
                   break;
               }
               case 26:
               {
                   Load_Inst(addr_inst, 0x33a02023);//65a02023
                   break;
               }
               case 27:
               {
                   Load_Inst(addr_inst, 0x33b02223);//65b02223
                   break;
               }
               case 28:
               {
                   Load_Inst(addr_inst, 0x33c02423);//65c02423
                   break;
               }
               case 29:
               {
                   Load_Inst(addr_inst, 0x33d02623);//65d02623
                   break;
               }
               case 30:
               {
                   Load_Inst(addr_inst, 0x33e02823);//65e02823
                   break;
               }
               case 31:
               {
                   Load_Inst(addr_inst, 0x33f02a23);//65f02a23
                   break;
               }
               default: printf("x%d can't be stored due to non-exist.\n", i);
           }
    }

    En_CPU((to_reg - from_reg + 1) + 3, 1);
    *addr_inst = *addr_inst + 3;

    //read D-Mem
    uint32_t base_addr_rd = 0x2BC; // 700

    for (int i=from_reg; i<=to_reg; i=i+1)
    {
        if (i > 0 && i <= 31)
        {
           Rd_Data('x', i, (i-1) * 4 + base_addr_rd);
        }
        else
           printf("x%d can't be read due to non-exist.\n", i);
    }

}
*/
/*
void Display_Float_Reg(uint32_t *addr_inst, int from_reg, int to_reg)
{
    //write D-Mem
    for(int i=from_reg; i<=to_reg; i=i+1)
    {
           switch(i)
           {
               case 1:
               {
                   Load_Inst(addr_inst, 0x32102e27);//64102c27
                   break;
               }
               case 2:
               {
                   Load_Inst(addr_inst, 0x34202027);//64202e27
                   break;
               }
               case 3:
               {
                   Load_Inst(addr_inst, 0x34302227);//66302027
                   break;
               }
               case 4:
               {
                   Load_Inst(addr_inst, 0x34402427);//66402227
                   break;
               }
               case 5:
               {
                   Load_Inst(addr_inst, 0x34502627);//66502427
                   break;
               }
               case 6:
               {
                   Load_Inst(addr_inst, 0x34602827);//66602627
                   break;
               }
               case 7:
               {
                   Load_Inst(addr_inst, 0x34702a27);//66702827
                   break;
               }
               case 8:
               {
                   Load_Inst(addr_inst, 0x34802c27);//66802a27
                   break;
               }
               case 9:
               {
                   Load_Inst(addr_inst, 0x34902e27);//66902c27
                   break;
               }
               case 10:
               {
                   Load_Inst(addr_inst, 0x36a02027);//66a02e27
                   break;
               }
               case 11:
               {
                   Load_Inst(addr_inst, 0x36b02227);//68b02027
                   break;
               }
               case 12:
               {
                   Load_Inst(addr_inst, 0x36c02427);//68c02227
                   break;
               }
               case 13:
               {
                   Load_Inst(addr_inst, 0x36d02627);//68d02427
                   break;
               }
               case 14:
               {
                   Load_Inst(addr_inst, 0x36e02827);//68e02627
                   break;
               }
               case 15:
               {
                   Load_Inst(addr_inst, 0x36f02a27);//68f02827
                   break;
               }
               case 16:
               {
                   Load_Inst(addr_inst, 0x37002c27);//69002a27
                   break;
               }
               case 17:
               {
                   Load_Inst(addr_inst, 0x37102e27);//69102c27
                   break;
               }
               case 18:
               {
                   Load_Inst(addr_inst, 0x39202027);//69202e27
                   break;
               }
               case 19:
               {
                   Load_Inst(addr_inst, 0x39302227);//6b302027
                   break;
               }
               case 20:
               {
                   Load_Inst(addr_inst, 0x39402427);//6b402227
                   break;
               }
               case 21:
               {
                   Load_Inst(addr_inst, 0x39502627);//6b502427
                   break;
               }
               case 22:
               {
                   Load_Inst(addr_inst, 0x39602827);//6b602627
                   break;
               }
               case 23:
               {
                   Load_Inst(addr_inst, 0x39702a27);//6b702827
                   break;
               }
               case 24:
               {
                   Load_Inst(addr_inst, 0x39802c27);//6b802a27
                   break;
               }
               case 25:
               {
                   Load_Inst(addr_inst, 0x39902e27);//6b902c27
                   break;
               }
               case 26:
               {
                   Load_Inst(addr_inst, 0x3ba02027);//6ba02e27
                   break;
               }
               case 27:
               {
                   Load_Inst(addr_inst, 0x3bb02227);//6db02027
                   break;
               }
               case 28:
               {
                   Load_Inst(addr_inst, 0x3bc02427);//6dc02227
                   break;
               }
               case 29:
               {
                   Load_Inst(addr_inst, 0x3bd02627);//6dd02427
                   break;
               }
               case 30:
               {
                   Load_Inst(addr_inst, 0x3be02827);//6de02627
                   break;
               }
               case 31:
               {
                   Load_Inst(addr_inst, 0x3bf02a27);//6df02827
                   break;
               }
               default: printf("f%d can't be stored due to non-exist.\n", i);
           }
    }

    En_CPU((to_reg - from_reg + 1) + 3, 1);
    *addr_inst = *addr_inst + 3;

    //read D-Mem
    uint32_t base_addr_rd = 0x33C; // 828
    for (int i=from_reg; i<=to_reg; i=i+1)
    {
        if (i > 0 && i <= 31)
        {
        	Rd_Data('f', i, (i-1) * 4 + base_addr_rd);
        }
        else
           printf("f%d can't be read due to non-exist.\n", i);
    }

}
*/
int main()
{
    //printf("Enter from keyboard: ");
    //c = XUartLite_RecvByte(uartRegAddr); //input from keyboard
    //c = XUartLite_RecvByte(uartRegAddr) - 0x30; //input char and convert to number
    //printf("%c\r\n", c + 0x30); // return value of var c, %c is char type
    //Xil_Out8(0x44a00000, data); // load data into address 0x44a00000
    //Xil_In8(0x44a00000); // export data from address 0x44a00000
    //xil_printf("\n", Xil_In8(0x44a00000));

    //CPU_IP_mWriteReg (XPAR_CPU_IP_0_S00_AXI_BASEADDR, 0x0, count);
    //CPU_IP_mReadReg  (XPAR_CPU_IP_0_S00_AXI_BASEADDR, RegOffset);

    //FILE *fptr;

    u32 baseaddr;
    baseaddr = (u32) XPAR_CPU_IP_0_S00_AXI_BASEADDR;

    init_platform();
    print("\nStart program\n\r");


    unsigned char c;
    uint32_t *addr_inst;
    *addr_inst = 0;

    uint32_t count[20];

    printf("Press r to RESET. \n\r");
    printf("Press i to out Int reg. \n\r");
    printf("Press f to out Float reg. \n\r");
    printf("Press 1 to check initial value. \n\r");
    printf("Press 2 to check Base integer case. \n\r");
    printf("Press 3 to check Base integer imm case. \n\r");
    printf("Press 4 to check Branch case. \n\r");
    printf("Press 5 to check Load store integer case. \n\r");
    printf("Press 6 to check Base float case. \n\r");
    printf("Press 7 to check Load store float case. \n\r");
    printf("Press 8 to check Structural Hazard case. \n\r");
    printf("Press 9 to check D-Cache operation case. \n\r");
    printf("Press c to check Move, Convert, Class case. \n\r");
    printf("Press t to check TRNG case. \n\r");
    printf("Press m to check MEM. \n\r");
    printf("Press e to EXIT. \n\n\r");


    printf("Make your select: ");
    c = XUartLite_RecvByte(uartRegAddr); // XUartLite_RecvByte(uartRegAddr) : hàm nhận giá trị từ bên ngoài
    while(c != 'e')
    {
        switch(c)
        {
               case 'r':
               {
            	  XUartLite_SendByte(uartRegAddr, c); //XUartLite_SendByte(uartRegAddr, c) : hàm xuất giá trị 'c', 'c' là giá trị đã nhập
            	  addr_inst = 0;
                  //Rst_CPU ();
                  //CPU_IP_mWriteReg (baseaddr, selftest_TRNG, 1);
                  printf("\nDone RESET.\n");
                  printf("\nMake your select: ");
                  break;
               }
               case 'i':
               {
            	  XUartLite_SendByte(uartRegAddr, c);
            	  //Display_Int_Reg (addr_inst, 1, 31);
            	  printf("\nMake your select: ");
            	  break;
               }
               case 'f':
               {
            	  XUartLite_SendByte(uartRegAddr, c);
            	  //Display_Float_Reg (addr_inst, 1, 31);
            	  printf("\nMake your select: ");
            	  break;
               }
/*               case 'd':
               {
                  printf("%c\r\n",c);
                  fptr = fopen("D:\\KhoaLuan\\Vivado_2019\\Ram\\I_Mem.txt", "r");
                  fscanf(fptr, str);
              	  printf("Read file: %x\r\n", str);
              	  fclose(fptr);
            	  printf("\nMake your select: ");
              	  break;
               }*/
               /*
               case '1'://Initial
               {
             	  XUartLite_SendByte(uartRegAddr, c);
                  // Init integer
                  Load_Inst(addr_inst, 0x00400093);//00400093
                  Load_Inst(addr_inst, 0x01000113);//01000113
                  Load_Inst(addr_inst, 0xbbc00193);//bbc00193
                  Load_Inst(addr_inst, 0xd8f00213);//d8f00213
                  Load_Inst(addr_inst, 0x04500293);//04500293
                  Load_Inst(addr_inst, 0xff000313);//ff000313
                  Load_Inst(addr_inst, 0x84900393);//84900393
                  Load_Inst(addr_inst, 0x01419413);//01419413

                  // Init float
                  Load_Inst(addr_inst, 0xd000f0d3);//d000f0d3
                  Load_Inst(addr_inst, 0xd0017153);//d0017153
                  Load_Inst(addr_inst, 0xd001f1d3);//d001f1d3
                  Load_Inst(addr_inst, 0xd0027253);//d0027253
                  Load_Inst(addr_inst, 0xd002f2d3);//d002f2d3
                  Load_Inst(addr_inst, 0xd0037353);//d0037353
                  Load_Inst(addr_inst, 0xd00473d3);//d00473d3
                  Load_Inst(addr_inst, 0xd0147453);//d0147453

                  // Init data_mem
                  Load_Inst(addr_inst, 0x00102023);//00102023
                  Load_Inst(addr_inst, 0x00202223);//00202223
                  Load_Inst(addr_inst, 0x00302423);//00302423
                  Load_Inst(addr_inst, 0x00402623);//00402623
                  Load_Inst(addr_inst, 0x00502823);//00502823
                  Load_Inst(addr_inst, 0x00602a23);//00602a23
                  Load_Inst(addr_inst, 0x00702c23);//00702c23
                  Load_Inst(addr_inst, 0x00802e23);//00802e23
                  Load_Inst(addr_inst, 0x08102027);//08102027
                  Load_Inst(addr_inst, 0x08202227);//08202227
                  Load_Inst(addr_inst, 0x08302427);//08302427
                  Load_Inst(addr_inst, 0x08402627);//08402627
                  Load_Inst(addr_inst, 0x08502827);//08502827
                  Load_Inst(addr_inst, 0x08602a27);//08602a27
                  Load_Inst(addr_inst, 0x08702c27);//08702c27
                  Load_Inst(addr_inst, 0x08802e27);//08802e27
                  Load_Inst(addr_inst, 0x10102023);//10102023
                  Load_Inst(addr_inst, 0x10202223);//10202223
                  Load_Inst(addr_inst, 0x10302423);//10302423
                  Load_Inst(addr_inst, 0x10402623);//10402623
                  Load_Inst(addr_inst, 0x10502823);//10502823
                  Load_Inst(addr_inst, 0x10602a23);//10602a23
                  Load_Inst(addr_inst, 0x10702c23);//10702c23
                  Load_Inst(addr_inst, 0x10802e23);//10802e23
                  Load_Inst(addr_inst, 0x18102027);//18102027
                  Load_Inst(addr_inst, 0x18202227);//18202227
                  Load_Inst(addr_inst, 0x18302427);//18302427
                  Load_Inst(addr_inst, 0x18402627);//18402627
                  Load_Inst(addr_inst, 0x18502827);//18502827
                  Load_Inst(addr_inst, 0x18602a27);//18602a27
                  Load_Inst(addr_inst, 0x18702c27);//18702c27
                  Load_Inst(addr_inst, 0x18802e27);//18802e27

                  // Init D-Cache
                  Load_Inst(addr_inst, 0x00002983);//00002983
                  Load_Inst(addr_inst, 0x00402983);//00402983
                  Load_Inst(addr_inst, 0x00802983);//00802983
                  Load_Inst(addr_inst, 0x00c02983);//00c02983
                  Load_Inst(addr_inst, 0x01002983);//01002983
                  Load_Inst(addr_inst, 0x01402983);//01402983
                  Load_Inst(addr_inst, 0x01802983);//01802983
                  Load_Inst(addr_inst, 0x01c02983);//01c02983
                  Load_Inst(addr_inst, 0x08002987);//08002987
                  Load_Inst(addr_inst, 0x08402987);//08402987
                  Load_Inst(addr_inst, 0x08802987);//08802987
                  Load_Inst(addr_inst, 0x08c02987);//08c02987
                  Load_Inst(addr_inst, 0x09002987);//09002987
                  Load_Inst(addr_inst, 0x09402987);//09402987
                  Load_Inst(addr_inst, 0x09802987);//09802987
                  Load_Inst(addr_inst, 0x09c02987);//09c02987
                  Load_Inst(addr_inst, 0x10002983);//10002983
                  Load_Inst(addr_inst, 0x10402983);//10402983
                  Load_Inst(addr_inst, 0x10802983);//10802983
                  Load_Inst(addr_inst, 0x10c02983);//10c02983
                  Load_Inst(addr_inst, 0x11002983);//11002983
                  Load_Inst(addr_inst, 0x11402983);//11402983
                  Load_Inst(addr_inst, 0x11802983);//11802983
                  Load_Inst(addr_inst, 0x11c02983);//11c02983
                  Load_Inst(addr_inst, 0x18002987);//18002987
                  Load_Inst(addr_inst, 0x18402987);//18402987
                  Load_Inst(addr_inst, 0x18802987);//18802987
                  Load_Inst(addr_inst, 0x18c02987);//18c02987
                  Load_Inst(addr_inst, 0x19002987);//19002987
                  Load_Inst(addr_inst, 0x19402987);//19402987
                  Load_Inst(addr_inst, 0x19802987);//19802987
                  Load_Inst(addr_inst, 0x19c02987);//19c02987


                  count[0] = *addr_inst;
                  En_CPU(count[0], 1);

                  printf("\nDone initial.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '2'://Base integer
               {
             	  XUartLite_SendByte(uartRegAddr, c);
                  // Non-hazard
             	  Load_Inst(addr_inst, 0x00208533);
             	  Load_Inst(addr_inst, 0x402185b3);
             	  Load_Inst(addr_inst, 0x00121633);
             	  Load_Inst(addr_inst, 0x005226b3);
             	  Load_Inst(addr_inst, 0x00523733);
             	  Load_Inst(addr_inst, 0x0051c7b3);
             	  Load_Inst(addr_inst, 0x0011d833);
             	  Load_Inst(addr_inst, 0x401258b3);
             	  Load_Inst(addr_inst, 0x0051e933);
             	  Load_Inst(addr_inst, 0x0051f9b3);
             	  // Hazard
             	  Load_Inst(addr_inst, 0x00208a33);
             	  Load_Inst(addr_inst, 0x403a0ab3);
             	  Load_Inst(addr_inst, 0x001a9b33);
             	  Load_Inst(addr_inst, 0x014b2bb3);
             	  Load_Inst(addr_inst, 0x015b3c33);
             	  Load_Inst(addr_inst, 0x014b4cb3);
             	  Load_Inst(addr_inst, 0x014cdd33);
             	  Load_Inst(addr_inst, 0x401c5db3);
             	  Load_Inst(addr_inst, 0x01acee33);
             	  Load_Inst(addr_inst, 0x01bcfeb3);

                  count[1] = *addr_inst;
                  En_CPU(count[1] - count[0], 1);

                  printf("\nDone base integer case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '3'://Base integer imm
               {
             	  XUartLite_SendByte(uartRegAddr, c);
                  // Non-hazard
             	  Load_Inst(addr_inst, 0xfa218513);
             	  Load_Inst(addr_inst, 0xfef12593);
             	  Load_Inst(addr_inst, 0xfef13613);
             	  Load_Inst(addr_inst, 0x4d224693);
             	  Load_Inst(addr_inst, 0x0d13e713);
             	  Load_Inst(addr_inst, 0x79e47793);
             	  Load_Inst(addr_inst, 0x00a11813);
             	  Load_Inst(addr_inst, 0x00425893);
             	  Load_Inst(addr_inst, 0x40425913);
             	  Load_Inst(addr_inst, 0x020029b7);
             	  Load_Inst(addr_inst, 0x02002497);

             	  // Hazard
             	  Load_Inst(addr_inst, 0xfa218a13);
             	  Load_Inst(addr_inst, 0x827a2a93);
             	  Load_Inst(addr_inst, 0x00ca3b13);
             	  Load_Inst(addr_inst, 0x4d2a4b93);
             	  Load_Inst(addr_inst, 0x12ebec13);
             	  Load_Inst(addr_inst, 0x7d6bfc93);
             	  Load_Inst(addr_inst, 0x002c9d13);
             	  Load_Inst(addr_inst, 0x004cdd93);
             	  Load_Inst(addr_inst, 0x405d5e13);


                  count[2] = *addr_inst;
                  En_CPU(count[2] - count[1], 1);

                  printf("\nDone base integer imm.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '4'://Branch
               {
                 XUartLite_SendByte(uartRegAddr, c);
                 // Non-hazard
                 Load_Inst(addr_inst, 0x00b50663);
                 Load_Inst(addr_inst, 0x01450663);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x01451463);
                 Load_Inst(addr_inst, 0x00b51463);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00a04663);
                 Load_Inst(addr_inst, 0x00054663);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x000a5663);
                 Load_Inst(addr_inst, 0x01405863);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00096463);
                 Load_Inst(addr_inst, 0x01256463);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x01207663);
                 Load_Inst(addr_inst, 0x00a97663);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);

                 //Hazard
                 Load_Inst(addr_inst, 0x07b00f13);
                 Load_Inst(addr_inst, 0x07b00f93);
                 Load_Inst(addr_inst, 0x000f0963);
                 Load_Inst(addr_inst, 0x01ff0663);
                 Load_Inst(addr_inst, 0x03400eef);
                 Load_Inst(addr_inst, 0x28cf8ee7);
                 Load_Inst(addr_inst, 0x1c800f13);
                 Load_Inst(addr_inst, 0x1c800f93);
                 Load_Inst(addr_inst, 0x01ef9463);
                 Load_Inst(addr_inst, 0x01f01463);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x07b00f13);
                 Load_Inst(addr_inst, 0x31500f93);
                 Load_Inst(addr_inst, 0x01efc663);
                 Load_Inst(addr_inst, 0xfdff4ce3);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0x03d00f13);
                 Load_Inst(addr_inst, 0x01000f93);
                 Load_Inst(addr_inst, 0x01efd663);
                 Load_Inst(addr_inst, 0xfdff52e3);
                 Load_Inst(addr_inst, 0x014e89e7);
                 Load_Inst(addr_inst, 0xffdffeef);
                 Load_Inst(addr_inst, 0x00000000);
                 Load_Inst(addr_inst, 0xff000f13);
                 Load_Inst(addr_inst, 0xffc00f93);
                 Load_Inst(addr_inst, 0x01efe863);
                 Load_Inst(addr_inst, 0xffff66e3);
                 Load_Inst(addr_inst, 0x01d9f463);
                 Load_Inst(addr_inst, 0x013ef463);
                 Load_Inst(addr_inst, 0x00000000);


                  count[3] = *addr_inst;
                  En_CPU(count[3] - count[2], 1);

                  printf("\nDone Branch.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '5'://Load store integer
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // Load, store integer (non-hazard)
             	  Load_Inst(addr_inst, 0x01900503);
             	  Load_Inst(addr_inst, 0x08e01583);
             	  Load_Inst(addr_inst, 0x08802603);
             	  Load_Inst(addr_inst, 0x08604683);
             	  Load_Inst(addr_inst, 0x00805703);
             	  Load_Inst(addr_inst, 0x24900da3);
             	  Load_Inst(addr_inst, 0x24901f23);
             	  Load_Inst(addr_inst, 0x26902023);
             	  // Load, store integer (hazard offset)
             	  Load_Inst(addr_inst, 0x00400e93);
             	  Load_Inst(addr_inst, 0x097e8a03);
             	  Load_Inst(addr_inst, 0x114e9a83);
             	  Load_Inst(addr_inst, 0x194eab03);
             	  Load_Inst(addr_inst, 0x00000993);
             	  Load_Inst(addr_inst, 0x26398223);
             	  Load_Inst(addr_inst, 0x26399523);
             	  Load_Inst(addr_inst, 0x2639a623);
             	  // Store integer (hazard data)
             	  Load_Inst(addr_inst, 0x00c00993);
             	  Load_Inst(addr_inst, 0x000384b3);
             	  Load_Inst(addr_inst, 0x269982a3);
             	  Load_Inst(addr_inst, 0x26999523);
             	  Load_Inst(addr_inst, 0x2699a623);
             	  // Store and load at the same address
             	  Load_Inst(addr_inst, 0x01000993);
             	  Load_Inst(addr_inst, 0x00028eb3);
             	  Load_Inst(addr_inst, 0x27d9a623);
             	  Load_Inst(addr_inst, 0x26c9a483);
             	  Load_Inst(addr_inst, 0x00048f13);
             	  Load_Inst(addr_inst, 0x00048f93);

                  count[4] = *addr_inst;
                  En_CPU(count[4] - count[3], 1);

                  printf("\nDone load store integer case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '6'://Base float
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // Base float (non-hazard)
             	  Load_Inst(addr_inst, 0x3020f543);
             	  Load_Inst(addr_inst, 0x3020f5c7);
             	  Load_Inst(addr_inst, 0x3020f64f);
             	  Load_Inst(addr_inst, 0x3020f6cb);
             	  Load_Inst(addr_inst, 0x00517753);
             	  Load_Inst(addr_inst, 0x085177d3);
             	  Load_Inst(addr_inst, 0x1022f853);
             	  Load_Inst(addr_inst, 0x1822f8d3);
             	  Load_Inst(addr_inst, 0x58017953);
             	  Load_Inst(addr_inst, 0x201309d3);
             	  Load_Inst(addr_inst, 0x20131a53);
             	  Load_Inst(addr_inst, 0x20132ad3);
             	  Load_Inst(addr_inst, 0x28608b53);
             	  Load_Inst(addr_inst, 0x28609bd3);
             	  Load_Inst(addr_inst, 0xa0612c53);
             	  Load_Inst(addr_inst, 0xa0611cd3);
             	  Load_Inst(addr_inst, 0xa0610d53);

             	  // Base float (hazard)
             	  Load_Inst(addr_inst, 0x0020f4d3);
             	  Load_Inst(addr_inst, 0x3090f543);
             	  Load_Inst(addr_inst, 0x5024f5c7);
             	  Load_Inst(addr_inst, 0x5895764f);
             	  Load_Inst(addr_inst, 0x5095f6cb);
             	  Load_Inst(addr_inst, 0x00c5f753);
             	  Load_Inst(addr_inst, 0x08d677d3);
             	  Load_Inst(addr_inst, 0x10977853);
             	  Load_Inst(addr_inst, 0x18e7f8d3);
             	  Load_Inst(addr_inst, 0x5807f953);
             	  Load_Inst(addr_inst, 0x211309d3);
             	  Load_Inst(addr_inst, 0x21131a53);
             	  Load_Inst(addr_inst, 0x20692ad3);
             	  Load_Inst(addr_inst, 0x295a0b53);
             	  Load_Inst(addr_inst, 0x296a1bd3);
             	  Load_Inst(addr_inst, 0xa16aac53);
             	  Load_Inst(addr_inst, 0xa17b1cd3);
             	  Load_Inst(addr_inst, 0xa19c0d53);

                  count[5] = *addr_inst;
                  En_CPU(count[5] - count[4], 1);

                  printf("\nDone base float case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '7'://Load store float
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // Load, store float (hazard offset)
             	  Load_Inst(addr_inst, 0x00400493);
             	  Load_Inst(addr_inst, 0x2694ae27);
             	  Load_Inst(addr_inst, 0x27c4a507);

             	  // Store float (hazard data)
             	  Load_Inst(addr_inst, 0x00800993);
             	  Load_Inst(addr_inst, 0x00027dd3);
             	  Load_Inst(addr_inst, 0x27b9ae27);
             	  // Store and load float at the same address
             	  Load_Inst(addr_inst, 0x00400993);
             	  Load_Inst(addr_inst, 0x0002fdd3);
             	  Load_Inst(addr_inst, 0x29b9a227);
             	  Load_Inst(addr_inst, 0x2849ae07);
             	  Load_Inst(addr_inst, 0x000e7ed3);
             	  Load_Inst(addr_inst, 0x000e7f53);

                  count[6] = *addr_inst;
                  En_CPU(count[6] - count[5], 1);

                  printf("\nDone load store float case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '8':// Structural Hazard
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // Structural Hazard
             	  Load_Inst(addr_inst, 0x08002803);
             	  Load_Inst(addr_inst, 0x08402883);
             	  Load_Inst(addr_inst, 0x01180933);

                  count[7] = *addr_inst;
                  En_CPU(count[7] - count[6], 1);

                  printf("\nDone Structural Hazard case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case '9':// D-Cache operation
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // D-Cache operation
             	  Load_Inst(addr_inst, 0x08700ca3);
             	  Load_Inst(addr_inst, 0x01802803);
             	  Load_Inst(addr_inst, 0x11802483);
             	  Load_Inst(addr_inst, 0x19802803);
             	  Load_Inst(addr_inst, 0x21002c23);
             	  Load_Inst(addr_inst, 0x21802403);
             	  Load_Inst(addr_inst, 0x11802803);

                  count[8] = *addr_inst;
                  En_CPU(count[8] - count[7], 1);

                  printf("\nDone D-Cache operation case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case 'c':// Move, convert, class
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // Move, convert, class
             	  Load_Inst(addr_inst, 0xf00181d3);
             	  Load_Inst(addr_inst, 0xe0010153);
             	  Load_Inst(addr_inst, 0xc0037253);
             	  Load_Inst(addr_inst, 0xc012f2d3);
             	  Load_Inst(addr_inst, 0xe00090d3);
             	  Load_Inst(addr_inst, 0x04500193);
             	  Load_Inst(addr_inst, 0x0010f1d3);
             	  Load_Inst(addr_inst, 0xf00181d3);

                  count[9] = *addr_inst;
                  En_CPU(count[9] - count[8], 1);

                  printf("\nDone Move, convert, class case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case 't'://TRNG
               {
             	  XUartLite_SendByte(uartRegAddr, c);
             	  // TRNG
             	  Load_Inst(addr_inst, 0x01501873);
             	  Load_Inst(addr_inst, 0x015018f3);
             	  Load_Inst(addr_inst, 0x01501973);

                  count[10] = *addr_inst;
                  En_CPU(3, 1);

                  printf("\nDone TRNG case.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
               case 'm'://MEM read
               {
             	  XUartLite_SendByte(uartRegAddr, c);
                  // Int
             	  Rd_Data('Mem ', 603, 600);
             	  Rd_Data('Mem ', 606, 604);
             	  Rd_Data('Mem ', 608, 608);

             	  Rd_Data('Mem ', 612, 612);
             	  Rd_Data('Mem ', 618, 616);
             	  Rd_Data('Mem ', 620, 620);

             	  Rd_Data('Mem ', 625, 624);
             	  Rd_Data('Mem ', 630, 628);
             	  Rd_Data('Mem ', 632, 632);

             	  Rd_Data('Mem ', 636, 636);

                  // Float
             	  Rd_Data('Mem ', 640, 640);

             	  Rd_Data('Mem ', 644, 644);

             	  Rd_Data('Mem ', 648, 648);

                  //D-Cache operation
             	  Rd_Data('Mem ', 153, 152);

             	  Rd_Data('Mem ', 536, 536);

                  printf("\nRead MEM.\r\n");

                  printf("\nMake your select: ");
                  break;
                }
				*/
               default: break;
         }

        c = XUartLite_RecvByte(uartRegAddr);
    }
    printf("End program %c\r\n");

    cleanup_platform();
    return 0;
}

