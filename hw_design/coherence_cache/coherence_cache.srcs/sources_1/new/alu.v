`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////

`include "riscv_define.vh"

module alu
(
    input  [3:0]      i_alu_control,
    input  [31:0]     i_alusrcA,
    input  [31:0]     i_alusrcB,
    output reg [31:0] o_alu_result,
    output reg [31:0] o_sign_bit
);

    always @(*) begin
        casex (i_alu_control)
            `ALU_ADD : {o_sign_bit, o_alu_result} = i_alusrcA + i_alusrcB;
            `ALU_SUB : {o_sign_bit, o_alu_result} = i_alusrcA - i_alusrcB;
            `ALU_SLL : {o_sign_bit, o_alu_result} = i_alusrcA << i_alusrcB;
            `ALU_SSUB: {o_sign_bit, o_alu_result} = $signed(i_alusrcA) - $signed(i_alusrcB);
            `ALU_USUB: {o_sign_bit, o_alu_result} = $unsigned(i_alusrcA) - $unsigned(i_alusrcB);
            `ALU_XOR : {o_sign_bit, o_alu_result} = i_alusrcA ^ i_alusrcB;
            `ALU_SRL : {o_sign_bit, o_alu_result} = $unsigned(i_alusrcA) >> $unsigned(i_alusrcB);
            `ALU_SRA : {o_sign_bit, o_alu_result} = $signed(i_alusrcA) >> $signed(i_alusrcB);
            `ALU_OR  : {o_sign_bit, o_alu_result} = i_alusrcA | i_alusrcB;
            `ALU_AND : {o_sign_bit, o_alu_result} = i_alusrcA & i_alusrcB;
            default  : {o_sign_bit, o_alu_result} = 0;
        endcase
    end
    
endmodule
