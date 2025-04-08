//////////////////////////////////////////////////////////////////////////////////
// this controller is used to control the access of requests coming from other Cache L1
//////////////////////////////////////////////////////////////////////////////////


module snoop_controller
(
    // system signals
    input   ACLK,
    input   ARESETn,
    
    // Snoop Response Channel
    // receive request from other Cache L1
    input   s_ACVALID,
    output  reg s_ACREADY,
    // input   [ADDR_WIDTH-1:0] s_ACADDR,
    input   [1:0] s_ACSNOOP,
    // send response to other Cache L1
    output  reg s_CVALID,
    input   s_CREADY,
    // output  [DATA_WIDTH-1:0] s_CDATA,
    output  reg s_CLAST,
    output  reg s_CHIT,
    
    // signals to control datapath
    // input from checker_port2_REG
    input   hit,
    output  reg state_tag_w_en,
    output  reg [3:0] control_offset,
    output  reg bus_in_reg_en
    // output  reg checker_port2_out_reg_en,
    // output  reg moesi_controller_out_reg_en
);
    
    // state definition
    localparam  IDLE     = 0;
    localparam  HIT_MISS = 1;
    localparam  RESP_BUS = 2;
    
    // variable to store state
    reg [1:0] state, next_state;
    
    // internal registers
    reg [3:0] sent_word_cnt;
    
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            state <= IDLE;
        end
        else begin
            state <= next_state;
        end
    end
    
    always @(*) begin
        case (state)
            IDLE: next_state = s_ACVALID ? HIT_MISS : IDLE;
            HIT_MISS: next_state = RESP_BUS;
            RESP_BUS: begin
                if (s_CREADY) begin
                    if (hit) begin
                        if (s_ACSNOOP == 2'b00) begin
                            next_state = (sent_word_cnt == 4'b1111) ? IDLE : RESP_BUS;
                        end
                        else
                        if (s_ACSNOOP == 2'b01) begin
                            next_state = (sent_word_cnt == 4'b1111) ? IDLE : RESP_BUS;
                        end
                        else 
                        if (s_ACSNOOP == 2'b10) begin
                            next_state = IDLE;
                        end
                        else begin
                            next_state = RESP_BUS;
                        end
                    end
                    else begin
                        next_state = IDLE;
                    end                    
                end
                else begin
                    next_state = RESP_BUS;
                end
            end
            default: next_state = IDLE;
        endcase
    end
    
    always @(*) begin
        case (state)
            IDLE:       begin
                s_ACREADY = 1;
                s_CVALID  = 0;
                s_CLAST   = 0;
                s_CHIT    = 0;
                state_tag_w_en = s_CLAST;
                control_offset = 4'b0000;
                bus_in_reg_en = 1;
                // checker_port2_out_reg_en = 0;
                // moesi_controller_out_reg_en = 0;
            end
            HIT_MISS:   begin
                s_ACREADY = 0;
                s_CVALID  = 0;
                s_CLAST   = 0;
                s_CHIT   = 0;
                state_tag_w_en = s_CLAST;
                control_offset = 4'b0000;
                bus_in_reg_en = 0;
                // checker_port2_out_reg_en = 1;
                // moesi_controller_out_reg_en = 0;
            end 
            RESP_BUS:   begin
                s_ACREADY = 0;
                s_CVALID  = 1;
                if (hit) begin
                    if (s_ACSNOOP == 2'b00) begin
                        s_CLAST = (sent_word_cnt == 4'b1111) ? 1 : 0;
                    end
                    else
                    if (s_ACSNOOP == 2'b01) begin
                        s_CLAST = (sent_word_cnt == 4'b1111) ? 1 : 0;
                    end
                    else 
                    if (s_ACSNOOP == 2'b10) begin
                        s_CLAST = 1;
                    end
                    else begin
                        s_CLAST = 0;
                    end
                    state_tag_w_en = s_CLAST;
                end
                else begin
                    s_CLAST = 1;
                    state_tag_w_en = 0;
                end
                s_CHIT = hit;
                control_offset = sent_word_cnt + 1;
                bus_in_reg_en = 0;
                // checker_port2_out_reg_en = 0;
                // moesi_controller_out_reg_en = 1;
            end
            default:    begin
                s_ACREADY = 0;
                s_CVALID  = 0;
                s_CLAST   = 0;
                s_CHIT    = 0;
                state_tag_w_en = s_CLAST;
                control_offset = 4'b0000;
                bus_in_reg_en = 0;
                // checker_port2_out_reg_en = 0;
                // moesi_controller_out_reg_en = 0;
            end
        endcase
    end
    
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            sent_word_cnt <= 4'b0000;
        end
        else begin
            if (next_state != state) begin
                sent_word_cnt <= 4'b0000;
            end
            else begin
                if (s_CREADY) begin
                    sent_word_cnt <= sent_word_cnt + 4'b0001;
                end
            end
        end
    end
    
endmodule
