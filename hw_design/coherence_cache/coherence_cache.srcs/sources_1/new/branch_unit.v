`timescale 1ns/1ps
module branch_unit(
    input               i_jump,
    input               i_jalr,
    input               i_branch,
    input [2:0]         i_funct3,
    input [4:0]         i_rs1,
    input [4:0]         i_rs2,

    input [4:0]         i_write_reg_EX,
    input               i_jump_EX,
    input               i_wb_EX,
    input               i_slt_EX,
    input [31:0]        i_pc_incr4_EX,
    input [31:0]        i_auipc_lui_data,
    input [31:0]        i_slt_data,
    input [31:0]        i_alu_result,

    input [4:0]         i_write_reg_MEM,
    input               i_jump_MEM,
    input               i_wb_MEM,
    input               i_slt_MEM,
    input               i_memread_MEM,
    input [31:0]        i_pc_incr4_MEM,
    input [31:0]        i_auipc_lui_data_MEM,
    input [31:0]        i_slt_data_MEM,
    input [31:0]        i_alu_result_MEM,
    input [31:0]        i_dataR_gen,

    input [4:0]         i_write_reg_WB,
    input               i_jump_WB,
    input               i_wb_WB,
    input               i_slt_WB,
    input [31:0]        i_pc_incr4_WB,
    input [31:0]        i_auipc_lui_data_WB,
    input [31:0]        i_slt_data_WB,
    input [31:0]        i_alu_result_WB,

    input [31:0]        i_dataA,
    input [31:0]        i_dataB,

    output reg [31:0]   o_rs1_data,
    output reg          o_pcsel1,
    output reg          o_pcsel2
);
  // pre-compute stage results
  wire [31:0] ex_data  = i_jump_EX ? i_pc_incr4_EX : i_wb_EX   ? i_auipc_lui_data : i_slt_EX ? i_slt_data : i_alu_result;
  wire [31:0] mem_data = i_jump_MEM? i_pc_incr4_MEM: i_wb_MEM  ? i_auipc_lui_data_MEM : i_slt_MEM ? i_slt_data_MEM : (i_memread_MEM?i_dataR_gen:i_alu_result_MEM);
  wire [31:0] wb_data  = i_jump_WB ? i_pc_incr4_WB  : i_wb_WB   ? i_auipc_lui_data_WB : i_slt_WB ? i_slt_data_WB : i_alu_result_WB;

  function [31:0] fwd(input [4:0] rs, input [31:0] rf_data);
    if(rs==i_write_reg_EX)      fwd=ex_data;
    else if(rs==i_write_reg_MEM)fwd=mem_data;
    else if(rs==i_write_reg_WB) fwd=wb_data;
    else                        fwd=rf_data;
  endfunction

  function compute_branch(input [2:0] fn, input [31:0] a,b);
    case(fn)
      3'b000: compute_branch=(a==b);
      3'b001: compute_branch=(a!=b);
      3'b100: compute_branch=($signed(a)<$signed(b));
      3'b101: compute_branch=($signed(a)>=$signed(b));
      3'b110: compute_branch=(a<b);
      3'b111: compute_branch=(a>=b);
      default:compute_branch=1'b0;
    endcase
  endfunction

  wire [31:0] rs1_val = fwd(i_rs1,i_dataA);
  wire [31:0] rs2_val = fwd(i_rs2,i_dataB);

  always @(*) begin
    o_pcsel1=0; o_pcsel2=0; o_rs1_data=0;
    if(i_jump) begin               // JAL/JALR
      o_pcsel1 = 1;
      o_pcsel2 = i_jalr;
      if(i_jalr) o_rs1_data = rs1_val;
    end else if(i_branch && compute_branch(i_funct3, rs1_val, rs2_val)) begin // BEQ/BNE/…
      o_pcsel1 = 1;
    end
  end
endmodule


//`timescale 1ns / 1ps

//module branch_unit (
//    input               i_jump,
//    input               i_jalr,
//    input               i_branch,
//    input [2:0]         i_funct3,
//    input [4:0]         i_rs1,
//    input [4:0]         i_rs2,

//    input [4:0]         i_write_reg_EX,
//    input               i_jump_EX,
//    input               i_wb_EX,
//    input               i_slt_EX,
//    input [31:0]        i_pc_incr4_EX,
//    input [31:0]        i_auipc_lui_data,
//    input [31:0]        i_slt_data,
//    input [31:0]        i_alu_result,

//    input [4:0]         i_write_reg_MEM,
//    input               i_jump_MEM,
//    input               i_wb_MEM,
//    input               i_slt_MEM,
//    input               i_memread_MEM,
//    input [31:0]        i_pc_incr4_MEM,
//    input [31:0]        i_auipc_lui_data_MEM,
//    input [31:0]        i_slt_data_MEM,
//    input [31:0]        i_alu_result_MEM,
//    input [31:0]        i_dataR_gen,

//    input [4:0]         i_write_reg_WB,
//    input               i_jump_WB,
//    input               i_wb_WB,
//    input               i_slt_WB,
//    input [31:0]        i_pc_incr4_WB,
//    input [31:0]        i_auipc_lui_data_WB,
//    input [31:0]        i_slt_data_WB,
//    input [31:0]        i_alu_result_WB,

//    input [31:0]        i_dataA,
//    input [31:0]        i_dataB,

//    output reg [31:0]   o_rs1_data,
//    output reg          o_pcsel1,
//    output reg          o_pcsel2
//);

//    function [31:0] forward_data;
//        input [4:0] rs;
//        input [4:0] reg_EX, reg_MEM, reg_WB;
//        input [31:0] data_EX, data_MEM, data_WB;
//        input valid_EX, valid_MEM, valid_WB;
//        begin
//            if (rs == reg_EX && valid_EX) forward_data = data_EX;
//            else if (rs == reg_MEM && valid_MEM) forward_data = data_MEM;
//            else if (rs == reg_WB && valid_WB) forward_data = data_WB;
//            else forward_data = (rs == i_rs1) ? i_dataA : i_dataB;
//        end
//    endfunction
    
//    function do_branch;
//        input [31:0] a, b;
//        input [2:0] funct3;
//        begin
//            case (funct3)
//                3'b000: do_branch = (a == b);           // beq
//                3'b001: do_branch = (a != b);           // bne
//                3'b100: do_branch = ($signed(a) < $signed(b)); // blt
//                3'b101: do_branch = ($signed(a) >= $signed(b)); // bge
//                3'b110: do_branch = (a < b);            // bltu
//                3'b111: do_branch = (a >= b);           // bgeu
//                default: do_branch = 1'b0;
//            endcase
//        end
//    endfunction
    
//    reg [31:0] rs1_fwd, rs2_fwd;
    
//    always @(*) begin
//        o_pcsel1 = 0;
//        o_pcsel2 = 0;
//        o_rs1_data = 0;
//        rs1_fwd = i_dataA;
//        rs2_fwd = i_dataB;
    
//        // Forwarding for rs1
//        if (i_rs1 == i_write_reg_EX) begin
//            if (i_jump_EX) rs1_fwd = i_pc_incr4_EX;
//            else if (i_wb_EX) rs1_fwd = i_auipc_lui_data;
//            else if (i_slt_EX) rs1_fwd = i_slt_data;
//            else rs1_fwd = i_alu_result;
//        end else if (i_rs1 == i_write_reg_MEM) begin
//            if (i_jump_MEM) rs1_fwd = i_pc_incr4_MEM;
//            else if (i_wb_MEM) rs1_fwd = i_auipc_lui_data_MEM;
//            else if (i_slt_MEM) rs1_fwd = i_slt_data_MEM;
//            else rs1_fwd = i_memread_MEM ? i_dataR_gen : i_alu_result_MEM;
//        end else if (i_rs1 == i_write_reg_WB) begin
//            if (i_jump_WB) rs1_fwd = i_pc_incr4_WB;
//            else if (i_wb_WB) rs1_fwd = i_auipc_lui_data_WB;
//            else if (i_slt_WB) rs1_fwd = i_slt_data_WB;
//            else rs1_fwd = i_alu_result_WB;
//        end
    
//        // Forwarding for rs2 (ch? c?n n?u là branch)
//        if (i_branch) begin
//            if (i_rs2 == i_write_reg_EX) begin
//                if (i_jump_EX) rs2_fwd = i_pc_incr4_EX;
//                else if (i_wb_EX) rs2_fwd = i_auipc_lui_data;
//                else if (i_slt_EX) rs2_fwd = i_slt_data;
//                else rs2_fwd = i_alu_result;
//            end else if (i_rs2 == i_write_reg_MEM) begin
//                if (i_jump_MEM) rs2_fwd = i_pc_incr4_MEM;
//                else if (i_wb_MEM) rs2_fwd = i_auipc_lui_data_MEM;
//                else if (i_slt_MEM) rs2_fwd = i_slt_data_MEM;
//                else rs2_fwd = i_memread_MEM ? i_dataR_gen : i_alu_result_MEM;
//            end else if (i_rs2 == i_write_reg_WB) begin
//                if (i_jump_WB) rs2_fwd = i_pc_incr4_WB;
//                else if (i_wb_WB) rs2_fwd = i_auipc_lui_data_WB;
//                else if (i_slt_WB) rs2_fwd = i_slt_data_WB;
//                else rs2_fwd = i_alu_result_WB;
//            end
//        end
    
//        if (i_jump) begin
//            o_pcsel1 = 1;
//            o_pcsel2 = i_jalr;
//            o_rs1_data = rs1_fwd;
//        end else if (i_branch) begin
//            o_pcsel2 = 0;
//            o_pcsel1 = do_branch(rs1_fwd, rs2_fwd, i_funct3);
//        end
//    end
    
//endmodule

//`timescale 1ns / 1ps
////////////////////////////////////////////////////////////////////////////////////
////
////////////////////////////////////////////////////////////////////////////////////

//(* keep_hierarchy = "yes" *)

//module branch_unit (
//    input               i_jump,
//    input               i_jalr,
//    input               i_branch,
//    input [2:0]         i_funct3,

//    input [4:0]         i_rs1,
//    input [4:0]         i_rs2,

//    input [4:0]         i_write_reg_EX,
//    input               i_jump_EX,
//    input               i_wb_EX,
//    input               i_slt_EX,
//    input [31:0]        i_pc_incr4_EX,
//    input [31:0]        i_auipc_lui_data,
//    input [31:0]        i_slt_data,
//    input [31:0]        i_alu_result,

//    input [4:0]         i_write_reg_MEM,
//    input               i_jump_MEM,
//    input               i_wb_MEM,
//    input               i_slt_MEM,
//    input               i_memread_MEM,
//    input [31:0]        i_pc_incr4_MEM,
//    input [31:0]        i_auipc_lui_data_MEM,
//    input [31:0]        i_slt_data_MEM,
//    input [31:0]        i_alu_result_MEM,
//    input [31:0]        i_dataR_gen,

//    input [4:0]         i_write_reg_WB,
//    input               i_jump_WB,
//    input               i_wb_WB,
//    input               i_slt_WB,
//    input [31:0]        i_pc_incr4_WB,
//    input [31:0]        i_auipc_lui_data_WB,
//    input [31:0]        i_slt_data_WB,
//    input [31:0]        i_alu_result_WB,

//    input [31:0]        i_dataA,
//    input [31:0]        i_dataB,

//    output reg [31:0]   o_rs1_data,
//    output reg          o_pcsel1,
//    output reg          o_pcsel2
//);

//    always @(*) begin
//        o_pcsel1    = 0;
//        o_pcsel2    = 0;
//        o_rs1_data  = 0;
//        if((!i_jump) && (!i_branch)) begin  // khong phai lenh nhay/re nhanh
//            o_pcsel1 = 0;
//            o_pcsel2 = 0;
//        end 
//        else begin
//            if(i_jump) begin 
//                if(i_jalr) begin      // jalr
//                    o_pcsel1 = 1;
//                    o_pcsel2 = 1;
//                    if(i_rs1 == i_write_reg_EX) begin       // get data from EX stage
//                        if(i_jump_EX) begin
//                            o_rs1_data = i_pc_incr4_EX;
//                        end
//                        else if(i_wb_EX) begin
//                            o_rs1_data = i_auipc_lui_data;
//                        end
//                        else if(i_slt_EX) begin
//                            o_rs1_data = i_slt_data;
//                        end
//                        else begin
//                            o_rs1_data = i_alu_result;
//                        end
//                    end
//                    else if(i_rs1 == i_write_reg_MEM) begin     // get data from MEM stage
//                        if(i_jump_MEM) begin
//                            o_rs1_data = i_pc_incr4_MEM;
//                        end
//                        else if(i_wb_MEM) begin
//                            o_rs1_data = i_auipc_lui_data_MEM;
//                        end
//                        else if(i_slt_MEM) begin
//                            o_rs1_data = i_slt_data_MEM;
//                        end
//                        else begin
//                            o_rs1_data = i_alu_result_MEM;
//                        end
//                    end 
//                    else if(i_rs1 == i_write_reg_WB) begin      // get data from WB stage
//                        if(i_jump_WB) begin
//                            o_rs1_data = i_pc_incr4_WB;
//                        end
//                        else if(i_wb_WB) begin
//                            o_rs1_data = i_auipc_lui_data_WB;
//                        end
//                        else if(i_slt_WB) begin
//                            o_rs1_data = i_slt_data_WB;
//                        end
//                        else begin
//                            o_rs1_data = i_alu_result_WB;
//                        end
//                    end 
//                    else begin
//                        o_rs1_data = i_dataA;
//                    end
//                end
//                else begin          // jal
//                    o_pcsel1 = 1;
//                    o_pcsel2 = 0;
//                    o_rs1_data = i_dataA;
//                end
//            end
//            else if (i_branch) begin      // nhom lenh branch: beq, bne, ...
//                o_pcsel2 = 0;
//                if ((i_rs1!=i_write_reg_EX)&&(i_rs2!=i_write_reg_EX)&&(i_rs1!=i_write_reg_MEM)&&(i_rs2!=i_write_reg_MEM)&&(i_rs1!=i_write_reg_MEM)&&(i_rs2!=i_write_reg_MEM)) begin
//                    case (i_funct3)
//                        3'b000: o_pcsel1 = i_dataA == i_dataB;//beq
//                        3'b001: o_pcsel1 = i_dataA != i_dataB;//bne
//                        3'b100: o_pcsel1 = $signed(i_dataA) < $signed(i_dataB); //blt
//                        3'b101: o_pcsel1 = $signed(i_dataA) >= $signed(i_dataB); //bge
//                        3'b110: o_pcsel1 = i_dataA < i_dataB; // bltu
//                        3'b111: o_pcsel1 = i_dataA >= i_dataB; //bgeu
//                        default: o_pcsel1 = 1'b0;
//                    endcase
//                end        
//                else if(i_rs1 == i_write_reg_EX || i_rs2 == i_write_reg_EX) begin    // xung dot tai tang EX
//                    if(i_jump_EX) begin
//                        if(i_rs1 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_pc_incr4_EX == i_dataB;//beq
//                                3'b001: o_pcsel1= i_pc_incr4_EX != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_pc_incr4_EX) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_pc_incr4_EX) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_pc_incr4_EX < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_pc_incr4_EX >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_pc_incr4_EX == i_dataA;//beq
//                                3'b001: o_pcsel1= i_pc_incr4_EX != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_pc_incr4_EX); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_pc_incr4_EX); //bge
//                                3'b110: o_pcsel1= i_dataA < i_pc_incr4_EX; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_pc_incr4_EX; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else if(i_wb_EX) begin
//                        if(i_rs1 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_auipc_lui_data == i_dataB;//beq
//                                3'b001: o_pcsel1= i_auipc_lui_data != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_auipc_lui_data) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_auipc_lui_data) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_auipc_lui_data < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_auipc_lui_data >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_auipc_lui_data == i_dataA;//beq
//                                3'b001: o_pcsel1= i_auipc_lui_data != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_auipc_lui_data); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_auipc_lui_data); //bge
//                                3'b110: o_pcsel1= i_dataA < i_auipc_lui_data; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_auipc_lui_data; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else if(i_slt_EX) begin
//                        if(i_rs1 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_slt_data == i_dataB;//beq
//                                3'b001: o_pcsel1= i_slt_data != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_slt_data) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_slt_data) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_slt_data < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_slt_data >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_slt_data == i_dataA;//beq
//                                3'b001: o_pcsel1= i_slt_data != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_slt_data); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_slt_data); //bge
//                                3'b110: o_pcsel1= i_dataA < i_slt_data; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_slt_data; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else begin
//                        if(i_rs1 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_alu_result == i_dataB;//beq
//                                3'b001: o_pcsel1= i_alu_result != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_alu_result) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_alu_result) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_alu_result < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_alu_result >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_EX) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_alu_result == i_dataA;//beq
//                                3'b001: o_pcsel1= i_alu_result != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_alu_result); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_alu_result); //bge
//                                3'b110: o_pcsel1= i_dataA < i_alu_result; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_alu_result; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                end
//                else if(i_rs1 == i_write_reg_MEM || i_rs2 == i_write_reg_MEM) begin     // xung dot tai tang MEM
//                    if(i_jump_MEM) begin
//                        if(i_rs1 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_pc_incr4_MEM == i_dataB;//beq
//                                3'b001: o_pcsel1= i_pc_incr4_MEM != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_pc_incr4_MEM) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_pc_incr4_MEM) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_pc_incr4_MEM < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_pc_incr4_MEM >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_pc_incr4_MEM == i_dataA;//beq
//                                3'b001: o_pcsel1= i_pc_incr4_MEM != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_pc_incr4_MEM); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_pc_incr4_MEM); //bge
//                                3'b110: o_pcsel1= i_dataA < i_pc_incr4_MEM; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_pc_incr4_MEM; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else if(i_wb_MEM) begin
//                        if(i_rs1 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_auipc_lui_data_MEM == i_dataB;//beq
//                                3'b001: o_pcsel1= i_auipc_lui_data_MEM != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_auipc_lui_data_MEM) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_auipc_lui_data_MEM) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_auipc_lui_data_MEM < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_auipc_lui_data_MEM >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_auipc_lui_data_MEM == i_dataA;//beq
//                                3'b001: o_pcsel1= i_auipc_lui_data_MEM != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_auipc_lui_data_MEM); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_auipc_lui_data_MEM); //bge
//                                3'b110: o_pcsel1= i_dataA < i_auipc_lui_data_MEM; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_auipc_lui_data_MEM; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else if(i_slt_MEM) begin
//                        if(i_rs1 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_slt_data_MEM == i_dataB;//beq
//                                3'b001: o_pcsel1= i_slt_data_MEM != i_dataB;//bne
//                                3'b100: o_pcsel1= $signed(i_slt_data_MEM) < $signed(i_dataB); //blt
//                                3'b101: o_pcsel1= $signed(i_slt_data_MEM) >= $signed(i_dataB); //bge
//                                3'b110: o_pcsel1= i_slt_data_MEM < i_dataB; // bltu
//                                3'b111: o_pcsel1= i_slt_data_MEM >= i_dataB; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= i_slt_data_MEM == i_dataA;//beq
//                                3'b001: o_pcsel1= i_slt_data_MEM != i_dataA;//bne
//                                3'b100: o_pcsel1= $signed(i_dataA) < $signed(i_slt_data_MEM); //blt
//                                3'b101: o_pcsel1= $signed(i_dataA) >= $signed(i_slt_data_MEM); //bge
//                                3'b110: o_pcsel1= i_dataA < i_slt_data_MEM; // bltu
//                                3'b111: o_pcsel1= i_dataA >= i_slt_data_MEM; //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                    else begin
//                        if(i_rs1 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen == i_dataB) : (i_alu_result_MEM == i_dataB);//beq
//                                3'b001: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen != i_dataB) : (i_alu_result_MEM != i_dataB);//bne
//                                3'b100: o_pcsel1= (i_memread_MEM) ? ($signed(i_dataR_gen) < $signed(i_dataB)) : ($signed(i_alu_result_MEM) < $signed(i_dataB)); //blt
//                                3'b101: o_pcsel1= (i_memread_MEM) ? ($signed(i_dataR_gen) >= $signed(i_dataB)) : ($signed(i_alu_result_MEM) >= $signed(i_dataB)); //bge
//                                3'b110: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen < i_dataB) : (i_alu_result_MEM < i_dataB); // bltu
//                                3'b111: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen >= i_dataB) : (i_alu_result_MEM >= i_dataB); //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else if(i_rs2 == i_write_reg_MEM) begin
//                            case (i_funct3)
//                                3'b000: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen == i_dataA) : (i_alu_result_MEM == i_dataA);//beq
//                                3'b001: o_pcsel1= (i_memread_MEM) ? (i_dataR_gen != i_dataA) : (i_alu_result_MEM != i_dataA);//bne
//                                3'b100: o_pcsel1= (i_memread_MEM) ? ($signed(i_dataA) < $signed(i_dataR_gen)) : ($signed(i_dataA) < $signed(i_alu_result_MEM)); //blt
//                                3'b101: o_pcsel1= (i_memread_MEM) ? ($signed(i_dataA) >= $signed(i_dataR_gen)) : ($signed(i_dataA) >= $signed(i_alu_result_MEM)); //bge
//                                3'b110: o_pcsel1= (i_memread_MEM) ? (i_dataA < i_dataR_gen) : (i_dataA < i_alu_result_MEM); // bltu
//                                3'b111: o_pcsel1= (i_memread_MEM) ? (i_dataA >= i_dataR_gen) : (i_dataA >= i_alu_result_MEM); //bgeu
//                                default: o_pcsel1 = 1'b0;
//                            endcase
//                        end
//                        else begin
//                            o_pcsel1 = 0;
//                        end
//                    end
//                end
//            end
//            else begin
//                o_pcsel1 = 0;
//            end
//        end
//    end
    
//endmodule