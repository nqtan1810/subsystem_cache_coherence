`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// register file module
//////////////////////////////////////////////////////////////////////////////////

// update register_file to read and write in the same clock
module register_file (
    input  wire        clk,
    input  wire        rst_n,        // Active-low reset
    input  wire        regwrite,
    input  wire [4:0]  write_reg,
    input  wire [31:0] write_data,
    input  wire [4:0]  rs1,
    input  wire [4:0]  rs2,
    output wire [31:0] read_data1,
    output wire [31:0] read_data2
);

    // Register file: 32 registers of 32 bits each
    reg [31:0] regfile [0:31];

    integer i;

    // Write and reset logic
    always @(posedge clk) begin
        if (!rst_n) begin
            for (i = 0; i < 32; i = i + 1)
                regfile[i] <= 32'b0;
        end 
        else if (regwrite && write_reg != 0) begin
            regfile[write_reg] <= write_data;
        end
    end

    // Combinational read with forwarding for same-cycle write-read
    assign read_data1 = (rs1 == 0) ? 32'b0 : (regwrite && (rs1 == write_reg)) ? write_data : regfile[rs1];

    assign read_data2 = (rs2 == 0) ? 32'b0 : (regwrite && (rs2 == write_reg)) ? write_data : regfile[rs2];

endmodule


//module register_file (
//    input  wire        clk,
//    input  wire        rst_n,        // Active-low reset
//    input  wire        regwrite,
//    input  wire [4:0]  write_reg,
//    input  wire [31:0] write_data,
//    input  wire [4:0]  rs1,
//    input  wire [4:0]  rs2,
//    output wire [31:0] read_data1,
//    output wire [31:0] read_data2
//);
//
//    // Register file: 32 registers of 32 bits each
//    reg [31:0] regfile [0:31];
//
//    integer i;
//
//    // Write and reset logic
//    always @(posedge clk) begin
//        if (!rst_n) begin
//            for (i = 0; i < 32; i = i + 1)
//                regfile[i] <= 32'b0;
//        end 
//        else if (regwrite && write_reg != 0) begin
//            regfile[write_reg] <= write_data;
//        end
//    end
//
//    // Combinational read
//    assign read_data1 = (rs1 != 0) ? regfile[rs1] : 32'b0;
//    assign read_data2 = (rs2 != 0) ? regfile[rs2] : 32'b0;
//
//endmodule


//module register_file (
//    input  wire        clk,
//    input  wire        regwrite,
//    input  wire [4:0]  write_reg,
//    input  wire [31:0] write_data,
//    input  wire [4:0]  rs1,
//    input  wire [4:0]  rs2,
//    output wire [31:0] read_data1,
//    output wire [31:0] read_data2
//);

//    // Register file: 32 registers of 32 bits each
//    reg [31:0] regfile [0:31];

//    // Write on rising clock edge
//    always @(posedge clk) begin
//        if (regwrite && write_reg != 0)
//            regfile[write_reg] <= write_data;
//    end

//    // Combinational read
//    assign read_data1 = (rs1 != 0) ? regfile[rs1] : 32'b0;
//    assign read_data2 = (rs2 != 0) ? regfile[rs2] : 32'b0;

//endmodule
