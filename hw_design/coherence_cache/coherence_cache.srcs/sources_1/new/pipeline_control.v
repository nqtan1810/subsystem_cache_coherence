`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// this module is used to control write enable of pipeline registers
//////////////////////////////////////////////////////////////////////////////////


module pipeline_control
(
    input       ACLK,
    input       ARESETn,
    input       i_memwrite_EX,
    input       i_memread_EX,
    input       i_d_BVALID,
    input       i_d_RVALID,
    input       i_d_RLAST,
    output  reg o_enable
);

    // state
    localparam ENABLE   = 0;
    localparam DISABLE  = 1;
    
    reg state, next_state;
    
    // state transition
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            state <= ENABLE;
        end
        else begin
            state <= next_state;
        end
    end
    
    // next state
    always @(*) begin
        case (state)
            ENABLE  : next_state = (i_memwrite_EX || i_memread_EX) ?  DISABLE : ENABLE;
            DISABLE : next_state = (i_d_BVALID || (i_d_RVALID && i_d_RLAST)) ? ENABLE : DISABLE;
            default : next_state = ENABLE;
        endcase
    end
    
    // output
    always @(*) begin
        case (state)
            ENABLE  : o_enable = 1;
            DISABLE : o_enable = 0;
            default : o_enable = 1;
        endcase
    end

endmodule
